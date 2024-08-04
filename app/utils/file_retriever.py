import requests
import os


def retrieve_file(download_url, file_name, force_download=False):
    """
    Retrieves the file if it already exists or downloads it from the given URL and save for future usage.

    :param download_url: The URL from which to download the file.
    :param file_name: The name of the file to save the downloaded content to.
    :param force_download: Optional parameter to force download even if the file already exists. Default is False.
    :return: The content retrieved from the URL if a download was performed, otherwise the content read from the existing file.
    """
    if force_download or not _check_file_exists(file_name):
        content = _retrieve_url_content(download_url)
        _write_content_to_file(file_name, content)

    file_path = os.path.join('data', f'{file_name}.csv')
    return file_path


def _retrieve_url_content(download_url):
    """
    Retrieves the content of the given URL.

    :param download_url: The URL of the content to retrieve
    :return: The content retrieved from the URL
    """
    try:
        response = requests.get(download_url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error connecting to the data server: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    else:
        return response.content


def _write_content_to_file(file_name, file_content):
    """
    Write content to a file.

    :param file_name: The name of the file (without extension).
    :type file_name: str
    :param file_content: The content to be written to the file.
    :type file_content: bytes
    :return: None
    """
    with open(os.path.join('data', f'{file_name}.csv'), 'wb') as file:
        file.write(file_content)


def _check_file_exists(file_name):
    """
    Check if a given file exists.

    :param file_name: The name of the file to check for existence.
    :return: True if the file exists, False otherwise.
    """
    file_path = os.path.join('data', f'{file_name}.csv')
    return os.path.exists(file_path)
