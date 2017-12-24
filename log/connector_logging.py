import logging
import logging.config

logging.config.fileConfig("/Users/zhaoyin/Work/document/Connector project/DjangoConnector/log/log.conf")

log = logging.getLogger("connectorLoggers")
