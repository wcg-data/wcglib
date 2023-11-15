import platform
import os
import sys
import glob
from log_utils import logger

class WCGClass:
    def get_os(self):
        os_name = platform.system()
        if os_name == 'Windows':
            return 'Windows'
        elif os_name == 'Linux':
            return 'Linux'
        elif os_name == 'Darwin':
            return 'Mac'
        else:
            return 'Unknown'
    
    def regular_find_folder(self, base_path, pattern):
        # 使用 glob 模块来进行模糊匹配
        search_pattern = os.path.join(base_path, pattern)
        folders = glob.glob(search_pattern)
        if folders:
            return folders[0]  # 返回找到的第一个匹配项
        else:
            sys.exit(f"{base_path}下未找到该文件夹: {pattern}")  # 如果没有找到匹配项，则退出

    def set_driver(self, url, browser):
        # project_dir = self.get_project_dir()
        project_dir = os.path.abspath("utils")
        driver_path = os.path.join(project_dir, 'driver')

        browser_options = {
            'chrome': (ChromeOptions, ChromeService, 'chromedriver', 'chromedriver'),
            'firefox': (FirefoxOptions, FirefoxService, 'geckodriver', 'geckodriver'),
            'edge': (EdgeOptions, EdgeService, 'edgedriver', 'msedgedriver')
        }

        if browser not in browser_options:
            sys.exit(f"不支持的浏览器: {browser}")

        options_class, service_class, driver_folder_name, driver_name = browser_options[browser]
        options = options_class()
        options.add_argument("--headless")  # Ensure GUI is off
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        user_agent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69'
        options.add_argument(user_agent)
        # 浏览器通用选项设置

        os_map = {
            'Linux': ('linux', ''),
            'Windows': ('win', '.exe'),
            'Mac': ('mac', '') 
        }

        current_os = self.get_os()
        if current_os not in os_map:
            sys.exit(f"不支持的操作系统: {current_os}")

        os_driver_folder_suffix, file_suffix = os_map[current_os]
        os_driver_folder =  self.regular_find_folder(driver_path, f'{driver_folder_name}*{os_driver_folder_suffix}*')
        driver_executable = f'{driver_name}{file_suffix}'
        driver_full_path = os.path.join(driver_path, os_driver_folder, driver_executable)

        service = service_class(executable_path=driver_full_path)

        driver = webdriver.Chrome(service=service, options=options) if browser == 'chrome' \
            else webdriver.Firefox(service=service, options=options) if browser == 'firefox' \
            else webdriver.Edge(service=service, options=options)

        driver.get(url)
        log.info(f'loading web page: {url}')
        return driver
l
        