from selene.support.jquery_style_selectors import s


class SecureArea(object):
    def __init__(self):
        self.logo = s("#content > div > h2")

    def logout(self):
        s("#content > div > a").click()