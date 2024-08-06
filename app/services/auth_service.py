from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext

from app.models.user_auth_model import UserAuth

registered_users = []


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    # Meaningless secret, fixed and versioned here for academic purposes only
    secret = 'CVMFvMEuV1uB1CrkF1q1pRH0mue9mwBiKleDmcD'

    def register_user(self, auth_details: UserAuth):
        if any(x['username'] == auth_details.username for x in registered_users):
            raise HTTPException(status_code=400, detail='Username already exists')

        hashed_password = self.get_password_hash(auth_details.password)
        registered_users.append({
            'username': auth_details.username,
            'password': hashed_password
        })

    def authenticate_user(self, auth_details: UserAuth):
        user = None

        for x in registered_users:
            if x['username'] == auth_details.username:
                user = x
                break

        if (user is None) or (not self.verify_password(auth_details.password, user['password'])):
            raise HTTPException(status_code=401, detail='Invalid credentials')

        token = self.encode_token(user['username'])

        return {'token': token}

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

    def encode_token(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id
        }

        return jwt.encode(payload, self.secret, algorithm='HS256')

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')
