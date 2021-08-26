import os
import logging
import logging.handlers

def createFolders(basedir, path):
  folders = path.split('/')
  basedir = BASE_DIR + basedir
  while len(folders) > 0:
    basedir = basedir + '/' + folders[0]
    if os.path.isdir(basedir) == False:
      os.makedirs(basedir)
    del folders[0]

def initLog(filename = None):
  if filename is None:
    filename = 'main_{}.log'.format(timezone.now().strftime('%Y%m%d%H%M%S'))
  createFolders('', 'logs')
  h = logging.handlers.RotatingFileHandler(
    filename = f'logs/{filename}',
    maxBytes = 200 * 1024 *1024,
    backupCount = 20
  )
  h.setFormatter(logging.Formatter('%(asctime)s %(module)s:%(lineno)d %(levelname)s %(message)s'))
  LOG = logging.getLogger()
  LOG.addHandler(h)
  LOG.setLevel(logging.DEBUG)
  return LOG
