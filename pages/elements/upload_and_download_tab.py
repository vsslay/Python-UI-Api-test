import time

from pages.base_page import BasePage
import os.path


class UploadAndDownloadTab(BasePage):

    URL = "https://demoqa.com/upload-download"

    DOWNLOAD_FILE_LOCATOR = "//*[@id='downloadButton']"
    UPLOAD_PICTURE_LOCATOR = "//*[@id='uploadFile']"
    ELEMENT_UPLOADED_CONFIRMATION_LOCATOR = "//p[@id]"

    DOWNLOADED_FILE_PATH = 'C:/Users/sapko/Desktop/Project/Framework/QAtools/downloads/sampleFile.jpeg'
    EXAMPLE_FILE_PATH = "C:/Users/sapko/Desktop/Project/Framework/QAtools/files_for_tests/avatar.jpg"

    def navigate(self):
        self.url_open(self.URL)

    def download_file(self):
        self.js_click(self.DOWNLOAD_FILE_LOCATOR)

    def check_file_downloaded(self):
        if os.path.exists(self.EXAMPLE_FILE_PATH):
            pass
        else:
            exit()

    def check_file_uploaded_and_downloaded(self):
        try:
            self.js_click(self.DOWNLOAD_FILE_LOCATOR)
            time.sleep(5)
            self.check_file_downloaded()
            self.upload_file(self.UPLOAD_PICTURE_LOCATOR, self.EXAMPLE_FILE_PATH)
            self.wait_for_element_presence(self.ELEMENT_UPLOADED_CONFIRMATION_LOCATOR)
            return True
        except Exception:
            return False
        finally:
            os.remove(self.DOWNLOADED_FILE_PATH)
