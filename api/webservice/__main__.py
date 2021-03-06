import sys

import server
import utils

utils.populate_plugins()

server.app.config.from_json(sys.argv[1])
server.validate_config()
server.setup_runners()

server.socketio.run(server.app, port=5000, debug=True, host="127.0.0.1")
server.teardown_runners()
