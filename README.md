# About this module

This is a simple proxy module with a Proxy class contains functions like get a random proxy for a specific protocol (http or https), and update the proxy file.

### Constructor arguments

    proxy_file_name - defalut is 'proxy_list.txt'
    proxy_update_file_name - default is 'proxy_update_list.txt'

### Functions

#### update_proxy_list()

    updates the proxy_list file with working proxies.
    returns none
    
#### random_proxy(protocol:str)

    protocol - a str containing http or https.
    returns a random proxy of given protocols.

#### random_proxy_dict(protocols:tuple)

    protocols - a tuple containing http or https or both.
    returns a dict with proxy or proxies of given protocols.
