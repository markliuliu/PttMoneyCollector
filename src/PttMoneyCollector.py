import logging

import PyPtt

logger = logging.getLogger("PttMoneyCollector")


class PttMoneyCollector:
    def __init__(self, account, password, board="Gossiping"):
        self.ptt_bot = PyPtt.API()
        self.account = account
        self.password = password
        self.board = board
        self.search_list = [(PyPtt.SearchType.KEYWORD, '發錢')]
        self.login()
        self.last_index = self.__get_newest_send_money_index()

    def login(self, retryCount=10, kick=True):
        try:
            self.ptt_bot.login(ptt_id=self.account, ptt_pw=self.password, kick_other_session=kick)
            return True
        except Exception as e:
            if retryCount > 0:
                logger.warning(f"login fail, retryCount={retryCount}")
                return self.login(retryCount - 1)
            else:
                logger.error("error occur while log in, " + e)
                return False

    def logout(self):
        self.ptt_bot.logout()

    def __get_newest_send_money_index(self):
        try:
            return self.ptt_bot.get_newest_index(board=self.board, index_type=PyPtt.NewIndex.BOARD,
                                                 search_list=self.search_list)
        except (PyPtt.LoginError, PyPtt.ConnectionClosed):
            logger.info("please log in again")
            self.login(kick=True)
            return self.get_newer_send_money_post()

    def get_newer_send_money_post(self):
        try:
            newest_index = self.__get_newest_send_money_index()
            result = {}
            logger.info(f"last_index={self.last_index}, newest_index={newest_index}")
            for index in range(self.last_index + 1, newest_index + 1):
                post_info = self.ptt_bot.get_post(board=self.board, index=index, search_list=self.search_list,
                                                  query=False)
                if "R: " in post_info["title"]:
                    continue
                result[post_info["aid"]] = post_info
            self.last_index = newest_index
            return result
        except (PyPtt.LoginError, PyPtt.ConnectionClosed):
            logger.info("please log in again")
            self.login(kick=True)
            return self.get_newer_send_money_post()

    def comment(self, article_aid, content):
        try:
            self.ptt_bot.comment(board=self.board, aid=article_aid, comment_type=PyPtt.CommentType.PUSH,
                                 content=content)
        except (PyPtt.LoginError, PyPtt.ConnectionClosed):
            logger.info("please log in again")
            self.login(kick=True)
            self.comment(article_aid, content)


if __name__ == '__main__':
    account = "iwtes"
    password = "09240924"
    last_index = 1250
    collector = PttMoneyCollector(account=account, password=password)
    try:
        posts = collector.get_newer_send_money_post()
        print(posts.keys())
        print(posts["1dIbnU_J"])
        collector.comment("1dIbnU_J", "可愛!")
    finally:
        collector.logout()
