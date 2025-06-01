# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The 'memorize' tool for several agents to affect session states."""

from datetime import datetime
import json
import os
from typing import Dict, Any

from google.adk.agents.callback_context import CallbackContext
from google.adk.sessions.state import State
from google.adk.tools import ToolContext

from sentiment_analysis.shared_libraries import constants

SAMPLE_SCENARIO_PATH = os.getenv(
    "THERAPY_PROFILE_PATH", "sentiment_analysis/profiles/empty_default.json"
)

def memorize_list(key: str, value: str, tool_context: ToolContext):
    """
    Memorize pieces of information.

    Args:
        key: the label indexing the memory to store the value.
        value: the information to be stored.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    mem_dict = tool_context.state
    if key not in mem_dict:
        mem_dict[key] = []
    if value not in mem_dict[key]:
        mem_dict[key].append(value)
    return {"status": f'Stored "{key}": "{value}"'}


def memorize(key: str, value: str, tool_context: ToolContext):
    """
    Memorize pieces of information, one key-value pair at a time.

    Args:
        key: the label indexing the memory to store the value.
        value: the information to be stored.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    mem_dict = tool_context.state
    mem_dict[key] = value
    return {"status": f'Stored "{key}": "{value}"'}


def forget(key: str, value: str, tool_context: ToolContext):
    """
    Forget pieces of information.

    Args:
        key: the label indexing the memory to store the value.
        value: the information to be removed.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    if tool_context.state[key] is None:
        tool_context.state[key] = []
    if value in tool_context.state[key]:
        tool_context.state[key].remove(value)
    return {"status": f'Removed "{key}": "{value}"'}


def _set_initial_states(source: Dict[str, Any], target: State | dict[str, Any]):
    """
    Setting the initial session state given a JSON object of states.

    Args:
        source: A JSON object of states.
        target: The session state object to insert into.
    """
    
    if constants.THERAPIST_INITIALIZED not in target:
        target.update(source)
        target[constants.THERAPIST_INITIALIZED] = True
        

        therapist_profile = source.get(constants.THERAPIST_PROFILE, {})
        
        if therapist_profile:
            target[constants.THERAPIST_PROFILE] = therapist_profile

        session_data = source.get(constants.SESSION_DATA, {})
        if session_data:
            target[constants.THERAPIST_INITIALIZED] = True
            target[constants.SESSION_DATA] = session_data
            target[constants.PATIENT_ID] = session_data.get(constants.PATIENT_ID, "")
            target[constants.SESSION_TYPE] = session_data.get(constants.SESSION_TYPE, "")
            target[constants.SESSION_DATE] = session_data.get(constants.SESSION_DATE, "")
            target[constants.SESSION_START_TIME] = session_data.get(constants.SESSION_START_TIME, "")
            target[constants.SESSION_DURATION] = session_data.get(constants.SESSION_DURATION, "")
        

def _load_precreated_itinerary(callback_context: CallbackContext):
    """
    Sets up the initial state from the empty default profile.
    Set this as a callback as before_agent_call of the root_agent.
    This gets called before the system instruction is constructed.

    Args:
        callback_context: The callback context.
    """    
    data = {}
    with open(SAMPLE_SCENARIO_PATH, "r") as file:
        data = json.load(file)
        print(f"\nLoading Initial State: {data}\n")

    _set_initial_states(data["state"], callback_context.state)