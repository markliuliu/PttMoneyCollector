import argparse
import logging
import time

import schedule

from LoggingConfig import configure_logging
from PttMoneyCollector import PttMoneyCollector
from QuestionAnswer import QuestionAnswer

configure_logging()

logger = logging.getLogger("main")


def task():
    logger.debug("task start")

    posts = collector.get_newer_send_money_post()
    if not posts:
        logger.info("There is no new post")
        return

    for key in posts.keys():
        post = posts[key]
        comment = question_answer.get_comment(context=post["content"])
        logging.info(f"Post title={post["title"]}, with comment={comment}")
        collector.comment(article_aid=key, content=comment)


def parse_input_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--account", help="Ptt account")
    parser.add_argument("--password", help="Ptt password")
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_input_arguments()
    collector = PttMoneyCollector(account=args.account, password=args.password)
    question_answer = QuestionAnswer()

    schedule.every(5).minutes.do(task)
    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            logger.error("Error happened when try to run task", e)
        time.sleep(1)
