from http.server import SimpleHTTPRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
from robot import francasterSpeech
from robot.francasterController import FrancasterController
from robot.allbotsController import AllbotsController


def register_francaster_xmlrpc_methods(server: SimpleXMLRPCServer):
    # Register the motor power command function.
    FrancasterController()
    server.register_function(FrancasterController.set_motor_position, 'FrancasterController.set_motor_position')
    server.register_function(FrancasterController.shift_motor_position, 'FrancasterController.shift_motor_position')
    server.register_function(FrancasterController.walk_n_steps, 'FrancasterController.walk_n_steps')
    server.register_function(FrancasterController.do_hi, 'FrancasterController.do_hi')
    server.register_function(FrancasterController.reset_position, 'FrancasterController.reset_position')
    server.register_function(FrancasterController.walk_n_steps_with_knee_lift,
                             'FrancasterController.FrancasterController.walk_n_steps_with_knee_lift')
    server.register_function(FrancasterController.do_yes, 'FrancasterController.do_yes')
    server.register_function(FrancasterController.do_no, 'FrancasterController.do_no')
    server.register_function(francasterSpeech.speak, 'FrancasterController.speak')
    server.register_function(francasterSpeech.repeat, 'FrancasterController.repeat')
    server.register_function(francasterSpeech.answer, 'FrancasterController.answer_question')

def register_allbots_xmlrpc_methods(server: SimpleXMLRPCServer):
    AllbotsController()
    server.register_function(AllbotsController.reset_position, 'AllbotsController.reset_position')


# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8080
    server = SimpleXMLRPCServer(("", port), RequestHandler)

    # Register standard XML-RPC methods.
    server.register_introspection_functions()

    register_francaster_xmlrpc_methods(server)
    register_allbots_xmlrpc_methods(server)

    # Start to server.
    server.serve_forever()
