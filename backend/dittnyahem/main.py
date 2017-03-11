from gevent.monkey import patch_all

patch_all()

import logging
import gevent
import sys

from dittnyahem import web

logger = logging.getLogger(__name__)
def main():
    web_port=5000
    web_debug=True
    log_level="DEBUG"

    logging.basicConfig(stream=sys.stdout, level=getattr(logging, log_level),
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    web_job = gevent.spawn(web.start_web, web_port, web_debug)
    web_job.join()


if __name__ == '__main__':
    main()
