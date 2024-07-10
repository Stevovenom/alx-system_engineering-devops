<<<<<<< HEAD
<title>0x0F. Load balancer</title>
<a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png"></a>
<br>
=======
0x0F. Load balancer
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png">
>>>>>>> 7d679dfeb3cb1299589257212818abfb0e576e22

<h1>The curl command is a tool to transfer data from or to a server, using one of the supported protocols (HTTP, HTTPS, FTP, etc.). Here’s the differentiation between the options -v and -sI: </h1><br>

# <code>curl -v <ip-address>:</code>

<p>Verbose Output: The -v (or --verbose) option makes curl verbose during the operation. It will provide detailed information about the request and response, including headers, body, and additional details about the request/response process.
<strong>Use Case:</strong> Useful for debugging or understanding the full details of the HTTP transaction.
<strong>Output:</strong> Shows the full request headers sent to the server, response headers received from the server, and the response body.<p>
<br>

# <code>curl -sI <ip-address>:</code><br>

<p>Silent and Headers Only: The -s (or --silent) option makes curl operate in silent mode. It hides progress meter and error messages. The -I (or --head) option requests the headers only from the server and not the body.<br>
<strong>Use Case:</strong> Useful when you only need to see the HTTP headers and not the content of the response, such as checking response codes or headers.
<strong>Output:</strong> Displays only the response headers without the response body.</p><br>


## Examples:

Verbose Output Example <br></br>
<code>
curl -v http://example.com
<code><br>
This will show detailed information about the request and response, including all headers and the response body.

Silent Headers Only Example:<br></br>

<code>
curl -sI http://example.com
</code><br>
This will only display the headers of the response, without any additional information or response body.

<br></br>
When considering <code>curl -v <ip-address></code> and <code>curl -sI <ip-address></code> in terms of request and response usage, here's how they differ and where each is typically used:
<br>
<h1><strong><code>curl -v <ip-address></code></strong></h1><br>
#Request:<br>

<strong>Usage:</strong> This command is used when you need to debug or understand the full HTTP transaction between the client and server.<br>
<strong>Request Details:</strong> It sends a normal HTTP request to the server and includes all the default headers and the requested resource's body.<br>
#Response:

<strong>Usage:</strong> Useful for troubleshooting or inspecting the complete response from the server.<br>
<strong>Response Details:</strong> It provides a detailed output of the entire HTTP transaction, including:<br>
1. Request line and headers sent to the server.
2. Response line and headers received from the server.
3 Response body content.
4. Additional verbose information about the connection and data transfer.
<br>
<h2>Example Scenario:</h2>
<strong>Debugging:</strong> If you're trying to debug why a particular request isn't working as expected or want to see the detailed headers and body being exchanged, you would use this command.<br>
<code>
curl -v http://example.com
</code>

<h1>
<code>
curl -sI <ip-address>
</code></h1>

#Request:

<strong>Usage:</strong> This command is used when you only need to fetch the headers of a resource, such as checking the status of a server or verifying HTTP headers.<br>
<strong>Request Details:</strong> It sends an HTTP HEAD request to the server, which requests only the headers of the specified resource and not the body.
#Response:

<strong>Usage:</strong> Useful for quickly checking the HTTP headers, response status, and other metadata without downloading the actual content of the resource.<br>
<strong>Response Details:</strong> It provides a concise output containing only the response headers, such as:
1. HTTP status code.
2. Headers like Content-Type, Content-Length, Server, etc.
3. No response body.
<br></br>

<h2>Example Scenario:</h>
Status Check: If you want to quickly check if a server is up, or inspect headers like Content-Type or Cache-Control without downloading the entire content, you would use this command.<br></br>

<code>curl -sI http://example.com</code>
#Summary:
curl -v <ip-address>: Used for detailed debugging and inspection of the full request-response cycle, including headers and body.<br>
curl -sI <ip-address>: Used for quickly checking response headers and status without downloading the content of the resource.<br>

The concepts to look at for this particular task are: <br>
1. <a href="https://intranet.alxswe.com/concepts/46">Load balancer </a>
2. <a href="https://intranet.alxswe.com/concepts/68">Web stack Debugging </a>
3. <a href="https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ">Introduction to load balancing and HAProxy </a>
4. <a href="https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw">HTTP header </a>
5. <a href="https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg">Debian/Ubuntu HAPROXY packages </a>
