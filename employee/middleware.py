import time
import logging

# Set up a standard Python logger
logger = logging.getLogger(__name__)

class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 1. Code to execute BEFORE the view is called
        start_time = time.time()
        user = request.user if request.user.is_authenticated else "Anonymous"
        
        # 2. Let the request continue to the view
        response = self.get_response(request)

        # 3. Code to execute AFTER the view is called
        duration = time.time() - start_time
        status_code = response.status_code
        path = request.path
        method = request.method

        # Log the details to your terminal
        print(f"--- [LOG] User: {user} | Method: {method} | Path: {path} | Status: {status_code} | Time: {duration:.2f}s ---")
        
        return response