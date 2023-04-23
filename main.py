"""
For development purpose only
"""

import os

import uvicorn
from pyngrok import ngrok


if __name__ == "__main__":
    PORT = 8005
    # Open a HTTP tunnel on the default port 80
    # <NgrokTunnel: "http://<public_sub>.ngrok.io" ->
    # "http://localhost:PORT">
    http_tunnel = ngrok.connect(PORT, bind_tls=True)
    public_url = http_tunnel.public_url
    os.environ['API_URL'] = public_url
    print("public URL", public_url)

    # Run the server
    uvicorn.run("app.app:app", port=PORT, host="127.0.0.1",
                log_level="info", reload=True)

    # Close the HTTP tunnel
    print("disconnect and kill the tunnel")
    ngrok.disconnect(http_tunnel.public_url)
    ngrok.kill()
