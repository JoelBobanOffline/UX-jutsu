# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from userge.logger import logging  # noqa
from Config import Config, get_version  # noqa
from userge.core import (  # noqa
    Userge, filters, Message, get_collection, pool)

userge = Userge()  # userge is the client name
