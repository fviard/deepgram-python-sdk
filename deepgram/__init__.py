# Copyright 2023-2024 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

# version
__version__ = "0.0.0"

# entry point for the deepgram python sdk
import logging
from .utils import VerboseLogger
from .utils import (
    NOTICE,
    SPAM,
    SUCCESS,
    VERBOSE,
    WARNING,
    ERROR,
    FATAL,
    CRITICAL,
    INFO,
    DEBUG,
    NOTSET,
)

from .client import Deepgram, DeepgramClient
from .client import DeepgramClientOptions, ClientOptionsFromEnv
from .client import (
    DeepgramError,
    DeepgramTypeError,
    DeepgramModuleError,
    DeepgramApiError,
    DeepgramUnknownApiError,
)
from .errors import DeepgramApiKeyError

# listen/read client
from .client import Listen, Read

# common
from .client import (
    TextSource,
    BufferSource,
    StreamSource,
    FileSource,
    UrlSource,
    Sentiment,
)
from .client import (
    OpenResponse,
    MetadataResponse,
    CloseResponse,
    UnhandledResponse,
    ErrorResponse,
)

# speect-to-text WS
from .client import LiveClient, AsyncLiveClient  # backward compat
from .client import ListenWebSocketClient, AsyncListenWebSocketClient
from .client import LiveTranscriptionEvents
from .client import LiveOptions, ListenWebSocketOptions
from .client import (
    # OpenResponse,
    LiveResultResponse,
    # MetadataResponse,
    SpeechStartedResponse,
    UtteranceEndResponse,
    # CloseResponse,
    # UnhandledResponse,
    # ErrorResponse,
)

# prerecorded
from .client import PreRecordedClient, AsyncPreRecordedClient  # backward compat
from .client import ListenRESTClient, AsyncListenRESTClient
from .client import (
    ListenRESTOptions,
    PrerecordedOptions,
    PreRecordedStreamSource,
    PrerecordedSource,
    ListenRestSource,
)
from .client import (
    AsyncPrerecordedResponse,
    PrerecordedResponse,
    SyncPrerecordedResponse,
)

# read
from .client import ReadClient, AsyncReadClient
from .client import AnalyzeClient, AsyncAnalyzeClient
from .client import (
    AnalyzeOptions,
    AnalyzeStreamSource,
    AnalyzeSource,
)
from .client import (
    AsyncAnalyzeResponse,
    AnalyzeResponse,
    SyncAnalyzeResponse,
)

# speak
from .client import (
    SpeakOptions,
    SpeakRESTOptions,
    # SpeakWebSocketOptions,
    # FileSource,
    SpeakRestSource,
    SpeakSource,
)
from .client import SpeakWebSocketEvents

## speak REST
from .client import (
    SpeakClient,  # backward compat
    SpeakRESTClient,
    AsyncSpeakRESTClient,
)

from .client import (
    SpeakResponse,  # backward compat
    SpeakRESTResponse,
)

# ## speak WebSocket
# from .client import (
#     SpeakWebSocketClient,
#     AsyncSpeakWebSocketClient,
# )
# from .client import (
#     SpeakWebSocketResponse,
#     # OpenResponse,
#     # MetadataResponse,
#     FlushedResponse,
#     # CloseResponse,
#     # UnhandledResponse,
#     WarningResponse,
#     # ErrorResponse,
# )

# manage
from .client import ManageClient, AsyncManageClient
from .client import (
    ProjectOptions,
    KeyOptions,
    ScopeOptions,
    InviteOptions,
    UsageRequestOptions,
    UsageSummaryOptions,
    UsageFieldsOptions,
)

# manage client responses
from .client import (
    Message,
    Project,
    ProjectsResponse,
    MembersResponse,
    Key,
    KeyResponse,
    KeysResponse,
    ScopesResponse,
    InvitesResponse,
    UsageRequest,
    UsageRequestsResponse,
    UsageSummaryResponse,
    UsageFieldsResponse,
    Balance,
    BalancesResponse,
    ModelsResponse,
    ModelResponse,
)

# selfhosted
from .client import (
    OnPremClient,
    AsyncOnPremClient,
    SelfHostedClient,
    AsyncSelfHostedClient,
)

# utilities
from .audio import Microphone, DeepgramMicrophoneError
from .audio import (
    LOGGING,
    CHANNELS,
    RATE,
    CHUNK,
)
