**wikibugs** is a project on Wikimedia Tool Labs which took other an old Perl based script to relay Bugzilla notifications to IRC.

The bot is currently alpha stage, being tested in a few IRC channels on freenode.net.

The entire project is Python 3.4 / asyncio based.


### Steps from change to IRC ###

1. User makes a change on [https://bugzilla.wikimedia.org/](Wikimedia Bugzilla)
2. Bugzilla sends an e-mail to the list [https://lists.wikimedia.org/mailman/listinfo/wikibugs-l](wikibugs-l@lists.wikimedia.org)
3. Tools mail server receives the e-mail. `.forward` pipes it to [/toredis.py](toredis.py)
4. toredis.py sends the e-mail to Redis ('PUBLISH')

The Redis step is useful because the mail and exec hosts are not necessarily the
same. Making them find eachother is also not completely trivial.

5. The IRC bot listens to events on Redis ('SUBSCRIBE')
6. The IRC bot receives the new e-mail
7. `bzparser.py` parses the e-mail into a dict
8. Asynchronously, `bzparser.py` retrieves real names for e-mail addresses.
   If no response is received within 30 seconds, the request is stopped. (`pywikibugs.parse_email.fixup_future`)
9. For each channel, `pywikibugs.send_messages` builds a message (via build_message) and dispatches it to the IRC channel

### Deploying ###

    cd src/pywikibugs && git pull && cd ~ && ./start.bash

This will kill the current SGE job and start a new one.

Please log this using ``!log tools.wikibugs <message>`` in #wikimedia-labs.

#### Emergency fixes ####
If you need to make any emergency adjustments, please remember to git commit & git review those.
git review is set up to ask for username and password -- please use your shell username and
the password at https://gerrit.wikimedia.org/r/#/settings/http-password to submit the change to
gerrit. Don't forget to +2/+2 & merge it!


### Adding a new channel ###

Adapt the `pywikibugs.channels` dict. The format is:

    <channel name> => (filter function, parameters for build_message)

The filter function gets the bug change dict passed as parameter.

e.g.

    {"#pywikipediabot": (lambda x: x.get("X-Bugzilla-Product", None) == "Pywikibot", {})}

will filter all Pywikibot bugs, without sending any special parameters to build_message.

    {"#somechannel": (lambda x: True, {'hide_product': True})}

would send all bugs to #somechannel, but hides the product names.
