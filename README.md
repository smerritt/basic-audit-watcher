This is a very simple object-audit watcher for OpenStack Swift. It is intended to be a skeleton on which authors can base their own watchers.

To use:

1. Install this with `python setup.py install`

2. In the object auditor configuration (probably `/etc/swift/object-auditor.conf` or `/etc/swift/object-server.conf`), have the following:

    ```
    [object-auditor]
    watchers = basic
    ```

3. Look for files in /tmp ending in ".auditlog".


If more functionality is required, make a local copy of this repository, rename the entry point to something other than "basic", and start typing.