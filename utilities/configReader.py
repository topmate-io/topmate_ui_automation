from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locator","username"))
# print(config.get("basic info","test_site_url"))


def readConfig(section,key):
    config = ConfigParser()
    config.read("./config/conf.ini")
    return config.get(section,key)
