# -- coding: UTF-8 -- 
class alert_is_present(object):
    """ Expect an alert to be present."""

    """判断当前页面的alert弹窗"""
    def __init__(self):
        pass

    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return alert
        except :
            return False