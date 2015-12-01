"""
The uwsgi Python module
=======================

The uWSGI server automagically adds a ``uwsgi`` module into your Python apps.

This is useful for configuring the uWSGI server, use its internal functions and get statistics (as well as detecting whether you're actually running under uWSGI).
"""


# Module-level globals
# --------------------

numproc = 0
"""The number of processes/workers currently running."""

buffer_size = 0
"""The current configured buffer size in bytes."""

started_on = 0
"""The Unix timestamp of uWSGI's startup."""

fastfuncs = {}
"""This is the dictionary used to define :doc:`FastFuncs`."""

applist = []
"""This is the list of applications currently configured."""

applications = {}
"""This is the dynamic applications dictionary."""

message_manager_marshal = lambda: None
"""The callable to run when the uWSGI server receives a marshalled message."""


magic_table = {}
"""The magic table of configuration placeholders."""


opt = {}
"""The current configuration options, including any custom placeholders."""


version = 'uwsgi stub'
"""The uWSGI version string"""


# Cache functions
# ---------------

def cache_get(key, cache_name=None):
    """Get a value from the cache.

    :param key: The cache key to read.
    :param cache_name: The name of the cache in multiple cache mode (can be in the form name@address). Optional.
    """


def cache_set(key, value, expire=None, cache_name=None):
    """Set a value in the cache.

    :param key: The cache key to write.
    :param value: The cache value to write.
    :param expire: Expiry time of the value, in seconds.
    :param cache_name: The name of the cache in multiple cache mode (can be in the form name@address). Optional.
    """


def cache_update(key, value, expire=None, cache_server=None):
    """Update cache"""


def cache_del(key, cache_name=None):
    """Delete the given cached value from the cache.

    :param key: The cache key to delete.
    :param cache_name: The name of the cache in multiple cache mode (can be in the form name@address). Optional.
    """


def cache_exists(key, cache_name=None):
    """Quickly check whether there is a value in the cache associated with the given key.

    :param key: The cache key to check.
    :param cache_name: The name of the cache in multiple cache mode (can be in the form name@address). Optional.
    """


def cache_clear():
    """Clear cache"""


# Queue functions
# ---------------

def queue_get():
    """Queue get"""


def queue_set():
    """Queue set"""


def queue_last():
    """Queue last"""


def queue_push():
    """Queue push"""


def queue_pull():
    """Queue pull"""


def queue_pop():
    """Queue pop"""


def queue_slot():
    """Queue slot"""


def queue_pull_slot():
    """Queue pull slot"""


# SNMP functions
# --------------

def snmp_set_community(str):
    """Sets the SNMP community string

    :param str: The string containing the new community value.
    """


def snmp_set_counter32(oidnum, value):
    """Snmp set counter32."""


def snmp_set_counter64(oidnum, value):
    """Snmp set counter64."""


def snmp_set_gauge(oidnum, value):
    """Sets the counter or gauge to a specific value.

    :param oidnum: An integer containing the oid number target.
    :param value: An integer containing the new value of the counter or gauge.
    """

def snmp_incr_counter32(oidnum, value):
    """Snmp incr counter32."""


def snmp_incr_counter64(oidnum, value):
    """Snmp incr counter64."""


def snmp_incr_gauge(oidnum, value):
    """Snmp incr gauge."""


def snmp_decr_counter32(oidnum, value):
    """Snmp decr counter32."""


def snmp_decr_counter64(oidnum, value):
    """Snmp decr counter64."""


def snmp_decr_gauge(oidnum, value):
    """Increases or decreases the counter or gauge by a specific amount.

    .. note:: uWSGI OID tree starts at 1.3.6.1.4.1.35156.17

    :param oidnum: An integer containing the oid number target.
    :param value: An integer containing the amount to increase or decrease the counter or gauge. If not specified the default is 1.
    """


# Spooler functions
# -----------------

def send_to_spooler(message_dict=None, spooler=None, priority=None, at=None, body=None, **kwargs):
    """Send data to the :doc:`Spooler`. Also known as `spool()`.

    .. note:: Any of the keyword arguments may also be passed in the message dictionary. This means they're reserved words, in a way...

    :param message_dict: The message (string keys, string values) to spool. Either this, or **kwargs may be set.
    :param spooler: The spooler (id or directory) to use.
    :param priority: The priority of the message. Larger = less important.
    :param at: The minimum UNIX timestamp at which this message should be processed.
    :param body: A binary (bytestring) body to add to the message, in addition to the message dictionary itself. Its value will be available in the key ``body`` in the message.
    """


def set_spooler_frequency(seconds):
    """Set how often the spooler runs."""


def spooler_jobs():
    """Spooler jobs."""


def spooler_pid():
    """Spooler pid."""


# Advanced methods
# ----------------

def send_message():
    """Send a generic message using :doc:`Protocol`.

    .. note:: Until version `2f970ce58543278c851ff30e52758fd6d6e69fdc` this function was called ``send_uwsgi_message()``.
    """


def route():
    """Route."""


def send_multi_message():
    """Send a generic message to multiple recipients using :doc:`Protocol`.

    .. note:: Until version `2f970ce58543278c851ff30e52758fd6d6e69fdc` this function was called ``send_multi_uwsgi_message()``.

    .. seealso:: :doc:`Clustering` for examples
    """


def reload():
    """Gracefully reload the uWSGI server stack.

    .. seealso:: :doc:`Reload`
    """


def stop():
    """Stop uWSGI"""


def workers():
    """Get a statistics dictionary of all the workers for the current server. A dictionary is returned.

    :rtype: dict
    """


def masterpid():
    """Return the process identifier (PID) of the uWSGI master process.

    :rtype: int
    """


def total_requests():
    """Returns the total number of requests managed so far by the pool of uWSGI workers.

    :rtype: int
    """


def get_option():
    """Get option."""

def getoption():
    """Get option."""


def set_option():
    """Set option."""

def setoption():
    """Set option."""


def sorry_i_need_to_block():
    """Sorry I need to block."""


def request_id():
    """Request id."""


def worker_id():
    """Worker id."""


def mule_id():
    """Mule id."""


def log():
    """Log."""


def log_this_request():
    """Log this request."""


def set_logvar():
    """Set logvar."""


def get_logvar():
    """Get logvar."""


def disconnect():
    """Disconnect."""


def grunt():
    """Grunt."""


def lock(locknum=0):
    """Lock.

    :param int locknum: The lock number to lock. Lock 0 is always available.
    """


def is_locked():
    """Is locked."""


def unlock(locknum=0):
    """Unlock.

    :param locknum: The lock number to unlock. Lock 0 is always available.
    """


def cl():
    """Cl."""


def setprocname():
    """Setprocname."""


def listen_queue():
    """Listen Queue."""


def register_signal(num, who, function):
    """Register Signal.

    :param num: the signal number to configure
    :param who: a magic string that will set which process/processes receive the signal.

      * ``worker``/``worker0`` will send the signal to the first available worker. This is the default if you specify an empty string.
      * ``workers`` will send the signal to every worker.
      * ``workerN`` (N > 0) will send the signal to worker N.
      * ``mule``/``mule0`` will send the signal to the first available mule. (See :doc:`Mules`)
      * ``mules`` will send the signal to all mules
      * ``muleN`` (N > 0) will send the signal to mule N.
      * ``cluster`` will send the signal to all the nodes in the cluster. Warning: not implemented.
      * ``subscribed`` will send the signal to all subscribed nodes. Warning: not implemented.
      * ``spooler`` will send the signal to the spooler.

      ``cluster`` and ``subscribed`` are special, as they will send the signal to the master of all cluster/subscribed nodes. The other nodes will have to define a local handler though, to avoid a terrible signal storm loop.

   :param function: A callable that takes a single numeric argument.
   """


def signal(num):
    """Signal

    :param num: the signal number to raise
    """


def signal_wait(signum=None):
    """Signal wait.

    Block the process/thread/async core until a signal is received. Use ``signal_received`` to get the number of the signal received.
    If a registered handler handles a signal, ``signal_wait`` will be interrupted and the actual handler will handle the signal.

    :param signum: Optional - the signal to wait for
    """


def signal_registered():
    """Signal registered."""


def signal_received():
    """Signal received.

    Get the number of the last signal received. Used in conjunction with ``signal_wait``.
    """


def add_file_monitor():
    """Add file monitor."""


def add_timer(signum, seconds):
    """Add timer.

    :param int signum: The signal number to raise.
    :param int seconds: The interval at which to raise the signal.
    """


def add_probe():
    """Add probe."""


def add_rb_timer(signum, seconds, iterations=0):
    """Add an user-space (red-black tree backed) timer.

    :param int signum: The signal number to raise.
    :param int seconds: The interval at which to raise the signal.
    :param int iterations: How many times to raise the signal. 0 (the default) means infinity.
    """


def add_cron(signal, minute, hour, day, month, weekday):
    """Add cron.

    For the time parameters, you may use the syntax ``-n`` to denote "every n". For instance ``hour=-2`` would declare the signal to be sent every other hour.

    :param signal: The signal number to raise.
    :param minute: The minute on which to run this event.
    :param hour: The hour on which to run this event.
    :param day: The day on which to run this event. This is "OR"ed with ``weekday``.
    :param month: The month on which to run this event.
    :param weekday: The weekday on which to run this event. This is "OR"ed with ``day``. (In accordance with the POSIX standard, 0 is Sunday, 6 is Monday)
    """


def add_var(key, value):
    """Add uwsgi variable ``key`` with value ``value``

    :param str key: Variable name
    :param str value: Variable value
    """


def register_rpc():
    """Register rpc."""


def rpc():
    """rpc."""


def rpc_list():
    """rpc list."""


def call():
    """Call."""


def sendfile():
    """Sendfile."""


def set_warning_message():
    """set_warning_message."""


def mem():
    """mem."""


def has_hook():
    """has_hook."""


def logsize():
    """logsize."""


def send_multicast_message():
    """send_multicast_message."""


def cluster_nodes():
    """cluster_nodes."""


def cluster_node_name():
    """cluster_node_name."""


def cluster():
    """cluster."""


def cluster_best_node():
    """cluster_best_node."""


def connect():
    """connect."""


def connection_fd():
    """connection_fd."""


def is_connected():
    """is_connected."""


def send():
    """send."""


def recv():
    """recv."""


def recv_block():
    """recv_block."""


def recv_frame():
    """recv_frame."""


def close():
    """Close."""


def i_am_the_spooler():
    """I am the spooler."""


def fcgi():
    """fcgi."""


def parsefile():
    """parsefile."""


def embedded_data(symbol_name):
    """Extracts a symbol from the uWSGI binary image.

    .. seealso:: :doc:`Embed`

    :param symbol_name: The symbol name to extract.
    """


def extract():
    """Extract."""


def mule_msg(string, id=None):
    """Send a message to a mule.

    :param string: The bytestring message to send.
    :param id: Optional - the mule ID to receive the message. If you do not specify an ID, the message will go to the first available programmed mule.
    """


def farm_msg():
    """Farm message."""


def mule_get_msg():
    """Block until a mule message is received and return it. This can be called from multiple threads in the same programmed mule.

    :return: A mule message, once one is received.
    :rtype: str
    """


def farm_get_msg():
    """farm_get_msg."""


def in_farm():
    """in_farm."""


def ready():
    """ready."""


def set_user_harakiri():
    """set_user_harakiri."""


# Async functions
# ---------------


def async_sleep(seconds):
    """Suspend handling the current request for ``seconds`` seconds and pass control to the next async core.

    :param seconds: Sleep time, in seconds.
    """


def async_connect():
    """async_connect."""


def async_send_message():
    """async_send_message."""


def green_schedule():
    """green_schedule."""


def suspend():
    """Suspend handling the current request and pass control to the next async core clamoring for attention."""


def wait_fd_read(fd, timeout=None):
    """Suspend handling the current request until there is something to be read on file descriptor ``fd``.
    May be called several times before yielding/suspending to add more file descriptors to the set to be watched.

    :param fd: File descriptor number.
    :param timeout: Optional timeout (infinite if omitted).
    """


def wait_fd_write(fd, timeout=None):
    """Suspend handling the current request until there is nothing more to be written on file descriptor ``fd``.
    May be called several times to add more file descriptors to the set to be watched.

    :param fd: File descriptor number.
    :param timeout: Optional timeout (infinite if omitted).
    """


# SharedArea functions
# --------------------


def sharedarea_read(pos, len):
    """Read a byte string from the uWSGI :doc:`SharedArea`.

    :param pos: Starting position to read from.
    :param len: Number of bytes to read.
    :return: Bytes read, or ``None`` if the shared area is not enabled or the read request is invalid.
    :rtype: bytes
    """


def sharedarea_write(pos, str):
    """Write a byte string into the uWSGI :doc:`SharedArea`.

    :param pos: Starting position to write to.
    :param str: Bytestring to write.
    :return: Number of bytes written, or ``None`` if the shared area is not enabled or the write could not be fully finished.
    :rtype: int
    """


def sharedarea_readbyte(pos):
    """Read a single byte from the uWSGI :doc:`SharedArea`.

    :param pos: The position to read from.
    :return: Bytes read, or ``None`` if the shared area is not enabled or the read request is invalid.
    :rtype: int
    """

def sharedarea_writebyte(pos, val):
    """Write a single byte into the uWSGI :doc:`SharedArea`.

    :param pos: The position to write the value to.:param val: The value to write.
    :type val: integer
    :return: The byte written, or ``None`` if the shared area is not enabled or the write request is invalid.
    :rtype: int
    """


def sharedarea_readlong(pos):
    """Read a 64-bit (8-byte) long from the uWSGI :doc:`SharedArea`.

    :param pos: The position to read from.
    :return: The value read, or ``None`` if the shared area is not enabled or the read request is invalid.
    :rtype: int
    """


def sharedarea_writelong(pos, val):
    """Write a 64-bit (8-byte) long into the uWSGI :doc:`SharedArea`.

    :param pos: The position to write the value to.:param val: The value to write.
    :type val: long
    :return: The value written, or ``None`` if the shared area is not enabled or the write request is invalid.
    :rtype: int
    """


def sharedarea_inclong(pos):
    """Atomically increment a 64-bit long value in the uWSGI :doc:`SharedArea`.

    :param pos: The position of the value.
    :type val: long
    :return: The new value at the given position, or ``None`` if the shared area is not enabled or the read request is invalid.
    :rtype: int
    """


# Erlang functions
# ----------------

def erlang_send_message(node, process_name, message):
    """erlang_send_message."""


def erlang_register_process(process_name, callable):
    """erlang_register_process."""


def erlang_recv_message(node):
    """erlang_recv_message."""


def erlang_connect(address):
    """erlang_connect.

    :return: File descriptor or -1 on error
    """


def erlang_rpc(node, module, function, argument):
    """erlang_rpc."""


def websocket_handshake(http_sec_websocket_key=None, http_origin=None):
    """Waits for websocket handshake.

    :param http_sec_websocket_key: Optional HTTP_SEC_WEBSOCKET_KEY
    :param http_origin: Optional HTTP_ORIGIN
    """


def websocket_send(data):
    """Send ``data`` to websocket.

    :param str data: data to send
    """


def websocket_send_binary(data):
    """Send ``data`` to websocket.

    :param data: data to send
    """


def websocket_recv():
    """Receive data from websocket.

    :return: The received data
    :rtype: str
    """


def websocket_recv_nb():
    """Receive data from websocket (non-blocking).

    :return: The received data
    :rtype: str
    """


raise ImportError("No module named 'uwsgi'")
