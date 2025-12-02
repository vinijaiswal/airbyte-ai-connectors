"""
Auto-generated cassette tests for Gong connector.

These tests are generated from cassette YAML files and test the connector
against recorded API responses.
"""

import pytest
from unittest.mock import AsyncMock, patch

from airbyte_ai_gong import GongConnector



@pytest.mark.asyncio
async def test_call_transcripts_by_id():
    """Retrieve transcript for a specific call by ID"""
    mock_response = {'requestId': '5qrmby2e8ylmm61ftya', 'records': {'totalRecords': 1, 'currentPageSize': 1, 'currentPageNumber': 0}, 'callTranscripts': [{'callId': '1220490555266799467', 'transcript': [{'speakerId': '923767253756941667', 'topic': None, 'sentences': [{'start': 0, 'end': 8300, 'text': 'Load your Shopify data into any data warehouses, lakes or databases in minutes in the format you need.'}, {'start': 8560, 'end': 37230, 'text': 'With post load transformation… with Airbyte, any Shopify user can manage data and consolidate it into a single data lake to generate global reports, or integrate with the different destinations, including cloud data warehouses, lakes, and databases, or to on premises storage to be exploited through the AI analysis.'}, {'start': 39690, 'end': 39890, 'text': 'You.'}]}, {'speakerId': '7149681351570709090', 'topic': None, 'sentences': [{'start': 39890, 'end': 40640, 'text': 'Receive.'}]}, {'speakerId': '923767253756941667', 'topic': None, 'sentences': [{'start': 40640, 'end': 44850, 'text': 'Full control over the data normalized schemes.'}]}, {'speakerId': '7149681351570709090', 'topic': None, 'sentences': [{'start': 45210, 'end': 51460, 'text': 'Transformation via T a T… create new connection easily.'}]}, {'speakerId': '7149681351570709090', 'topic': None, 'sentences': [{'start': 55950, 'end': 79990, 'text': 'Select streams for replication… setup source in minutes… select the destination from the long list of different destinations… and get your data, combine it with the different data from the different…'}]}]}]}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.call_transcripts.list(filter={'callIds': ['1220490555266799467']})

    assert result == mock_response


@pytest.mark.asyncio
async def test_call_transcripts_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'requestId': '4sxr43rvxn7iqdr7yck', 'records': {'totalRecords': 4, 'currentPageSize': 4, 'currentPageNumber': 0}, 'callTranscripts': [{'callId': '8314721107404864518', 'transcript': [{'speakerId': '1894188309034628288', 'topic': None, 'sentences': [{'start': 1170, 'end': 6600, 'text': 'Hi, welcome to this demo demonstrating how you can move your Shopify data using Airbyte to your data warehouse of choice.'}, {'start': 7290, 'end': 11740, 'text': "Let's first log in with our test account credentials."}, {'start': 14430, 'end': 15770, 'text': "You'll be taken to the setting screen."}, {'start': 16170, 'end': 21650, 'text': "Let's select sources and create a new Shopify source."}, {'start': 22870, 'end': 36820, 'text': "So the you'll enter your Shopify store name… authenticate, via."}]}, {'speakerId': '1894188309034628288', 'topic': None, 'sentences': [{'start': 45990, 'end': 47840, 'text': 'The app is already authenticated on this account.'}, {'start': 47980, 'end': 49960, 'text': 'So I was able to do that successfully.'}, {'start': 53160, 'end': 56230, 'text': 'And then we just choose a start date for when we want to replicate data.'}]}, {'speakerId': '1894188309034628288', 'topic': None, 'sentences': [{'start': 68040, 'end': 79380, 'text': 'Once we click the setup button, Airbyte is verifying that all the parameters entered were correct and that the user has access to the Shopify store that they are requesting to move data from.'}]}, {'speakerId': '1894188309034628288', 'topic': None, 'sentences': [{'start': 86030, 'end': 86290, 'text': 'Okay.'}, {'start': 86550, 'end': 89660, 'text': 'So with that out of the way, we need to choose where we want to move our data.'}, {'start': 90320, 'end': 92280, 'text': "We've already set up a Postgres database here."}, {'start': 92930, 'end': 95360, 'text': "So I'll just select that."}, {'start': 96740, 'end': 111770, 'text': "And so as we're doing that and moving the connection and setting up the connection, we'll notice that Airbyte prompts us to choose which streams or which endpoints from the Shopify API we want to move."}, {'start': 111850, 'end': 118450, 'text': "So you'll see here we have abandoned checkouts, balance, transactions, collects custom collections, customers, and so on, and so forth."}, {'start': 119760, 'end': 125070, 'text': "So let's just sync a simple one."}, {'start': 126050, 'end': 130700, 'text': "So we'll select everything and then let's just select customers, for example."}, {'start': 131410, 'end': 136400, 'text': "And now we'll just move the customers… endpoint."}, {'start': 136520, 'end': 139430, 'text': 'So this will move all of our Shopify customers to post grass.'}, {'start': 139960, 'end': 141380, 'text': "And then we'll set up this connection."}]}, {'speakerId': '1894188309034628288', 'topic': None, 'sentences': [{'start': 147710, 'end': 152640, 'text': 'So you can see that the connection was set up correctly, if I click through, the sync is running.'}, {'start': 153160, 'end': 161030, 'text': 'And after some time, you will be able to log into the Postgres database that you set up and find your Shopify data for query.'}]}]}, {'callId': '5755144421565614827', 'transcript': []}, {'callId': '6204943119563513387', 'transcript': [{'speakerId': '7618404175166173034', 'topic': None, 'sentences': [{'start': 0, 'end': 2780, 'text': 'This is a demo for API connector.'}, {'start': 3280, 'end': 14100, 'text': 'Sorry, this, so, so if we need to create new connection… tab, some name.'}]}, {'speakerId': '7618404175166173034', 'topic': None, 'sentences': [{'start': 18540, 'end': 19930, 'text': 'Select the source type.'}]}, {'speakerId': '7618404175166173034', 'topic': None, 'sentences': [{'start': 29490, 'end': 36780, 'text': 'Start date… and state our account.'}]}, {'speakerId': '7618404175166173034', 'topic': None, 'sentences': [{'start': 45450, 'end': 47040, 'text': 'Authentication was succeeded.'}, {'start': 48150, 'end': 57790, 'text': "And as a source have also all connections tests what's… best has a… destination."}, {'start': 58630, 'end': 74580, 'text': "I'll use a local destination like CSV… and I select local CSV destination… type our destination boss."}]}, {'speakerId': '7618404175166173034', 'topic': None, 'sentences': [{'start': 80140, 'end': 87140, 'text': 'And destination… also connection test was past there.'}, {'start': 87560, 'end': 91040, 'text': 'I select cna frequency like manual.'}, {'start': 91600, 'end': 91860, 'text': 'There.'}, {'start': 92120, 'end': 93900, 'text': 'All of our streams serve page.'}, {'start': 93980, 'end': 99350, 'text': 'Sorry, question or response tests, all servers and set up connections.'}, {'start': 101530, 'end': 107340, 'text': 'There is our connection survey monkey to no sync yet.'}, {'start': 107840, 'end': 115690, 'text': 'But I now create an… and we have.'}]}, {'speakerId': '7618404175166173034', 'topic': None, 'sentences': [{'start': 121660, 'end': 148220, 'text': "So we can see that our sync was succeeded streams was sync and we can find in survey an older, our all CSV files is data… for example, it's survey streams is all our service."}, {'start': 148990, 'end': 150250, 'text': 'Thank you very much.'}]}]}, {'callId': '1220490555266799467', 'transcript': [{'speakerId': '923767253756941667', 'topic': None, 'sentences': [{'start': 0, 'end': 8300, 'text': 'Load your Shopify data into any data warehouses, lakes or databases in minutes in the format you need.'}, {'start': 8560, 'end': 37230, 'text': 'With post load transformation… with Airbyte, any Shopify user can manage data and consolidate it into a single data lake to generate global reports, or integrate with the different destinations, including cloud data warehouses, lakes, and databases, or to on premises storage to be exploited through the AI analysis.'}, {'start': 39690, 'end': 39890, 'text': 'You.'}]}, {'speakerId': '7149681351570709090', 'topic': None, 'sentences': [{'start': 39890, 'end': 40640, 'text': 'Receive.'}]}, {'speakerId': '923767253756941667', 'topic': None, 'sentences': [{'start': 40640, 'end': 44850, 'text': 'Full control over the data normalized schemes.'}]}, {'speakerId': '7149681351570709090', 'topic': None, 'sentences': [{'start': 45210, 'end': 51460, 'text': 'Transformation via T a T… create new connection easily.'}]}, {'speakerId': '7149681351570709090', 'topic': None, 'sentences': [{'start': 55950, 'end': 79990, 'text': 'Select streams for replication… setup source in minutes… select the destination from the long list of different destinations… and get your data, combine it with the different data from the different…'}]}]}]}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.call_transcripts.list(filter={'fromDateTime': '2023-01-01T00:00:00-08:00', 'toDateTime': '2025-11-20T23:59:59-08:00'})

    assert result == mock_response


@pytest.mark.asyncio
async def test_calls_get_id_1220490555266799467():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'requestId': '4k93dujm2p3lqdzusou', 'call': {'id': '1220490555266799467', 'url': 'https://us-20768.app.gong.io/call?id=1220490555266799467', 'title': 'Shopify ETL Open-source Data Integration Airbyte', 'scheduled': '2023-04-11T14:37:55.717888+03:00', 'started': '2023-04-11T14:37:55.717888+03:00', 'duration': 80, 'primaryUserId': '361458326017907882', 'direction': 'Unknown', 'system': 'Uploaded Call', 'scope': 'Unknown', 'media': 'Video', 'language': 'eng', 'workspaceId': '9196197544788600771', 'sdrDisposition': None, 'clientUniqueId': None, 'customData': None, 'purpose': None, 'meetingUrl': 'https://gong-import-meetings.s3.amazonaws.com/filestack/QHpV7HNgQP63MQqqZ4gq_Shopify%20ETL%20Open-source%20Data%20Integration%20Airbyte.mp4', 'isPrivate': False, 'calendarEventId': None}}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.calls.get(id="1220490555266799467")

    assert result == mock_response


@pytest.mark.asyncio
async def test_calls_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'requestId': '69jza7c7hggmqbtixym', 'records': {'totalRecords': 4, 'currentPageSize': 4, 'currentPageNumber': 0}, 'calls': [{'id': '1220490555266799467', 'url': 'https://us-20768.app.gong.io/call?id=1220490555266799467', 'title': 'Shopify ETL Open-source Data Integration Airbyte', 'scheduled': '2023-04-11T14:37:55.717888+03:00', 'started': '2023-04-11T14:37:55.717888+03:00', 'duration': 80, 'primaryUserId': '361458326017907882', 'direction': 'Unknown', 'system': 'Uploaded Call', 'scope': 'Unknown', 'media': 'Video', 'language': 'eng', 'workspaceId': '9196197544788600771', 'sdrDisposition': None, 'clientUniqueId': None, 'customData': None, 'purpose': None, 'meetingUrl': 'https://gong-import-meetings.s3.amazonaws.com/filestack/QHpV7HNgQP63MQqqZ4gq_Shopify%20ETL%20Open-source%20Data%20Integration%20Airbyte.mp4', 'isPrivate': False, 'calendarEventId': None}, {'id': '5755144421565614827', 'url': 'https://us-20768.app.gong.io/call?id=5755144421565614827', 'title': 'Airbyte - Youtube Analytics', 'scheduled': '2023-04-11T14:20:36.499211+03:00', 'started': '2023-04-11T14:20:36.499211+03:00', 'duration': 253, 'primaryUserId': '361458326017907882', 'direction': 'Unknown', 'system': 'Uploaded Call', 'scope': 'Unknown', 'media': 'Video', 'language': 'und', 'workspaceId': '9196197544788600771', 'sdrDisposition': None, 'clientUniqueId': None, 'customData': None, 'purpose': None, 'meetingUrl': 'https://gong-import-meetings.s3.amazonaws.com/filestack/sUik9oRTz23t8gjjen20_Airbyte%20-%20Youtube%20Analytics.mp4', 'isPrivate': False, 'calendarEventId': None}, {'id': '6204943119563513387', 'url': 'https://us-20768.app.gong.io/call?id=6204943119563513387', 'title': 'surveymonkey', 'scheduled': '2023-04-11T14:37:37.029699+03:00', 'started': '2023-04-11T14:37:37.029699+03:00', 'duration': 153, 'primaryUserId': '361458326017907882', 'direction': 'Unknown', 'system': 'Uploaded Call', 'scope': 'Unknown', 'media': 'Video', 'language': 'eng', 'workspaceId': '9196197544788600771', 'sdrDisposition': None, 'clientUniqueId': None, 'customData': None, 'purpose': None, 'meetingUrl': 'https://gong-import-meetings.s3.amazonaws.com/filestack/b7tRmr3HQOqUUJ8hgp3j_surveymonkey.mp4', 'isPrivate': False, 'calendarEventId': None}, {'id': '8314721107404864518', 'url': 'https://us-20768.app.gong.io/call?id=8314721107404864518', 'title': 'Y2Mate.is - Airbyte Shopify Demo-yIH6j1 idHw-480p-1655687813547', 'scheduled': '2023-04-11T14:38:16.164871+03:00', 'started': '2023-04-11T14:38:16.164871+03:00', 'duration': 163, 'primaryUserId': '361458326017907882', 'direction': 'Unknown', 'system': 'Uploaded Call', 'scope': 'Unknown', 'media': 'Video', 'language': 'eng', 'workspaceId': '9196197544788600771', 'sdrDisposition': None, 'clientUniqueId': None, 'customData': None, 'purpose': None, 'meetingUrl': 'https://gong-import-meetings.s3.amazonaws.com/filestack/9i2gAiRDQtuUkaUuKhlc_Y2Mate.is%20-%20Airbyte%20Shopify%20Demo-yIH6j1_idHw-480p-1655687813547.mp4', 'isPrivate': False, 'calendarEventId': None}]}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.calls.list(fromDateTime="2023-01-01T00:00:00-08:00", toDateTime="2025-11-20T23:59:59-08:00")

    assert result == mock_response


@pytest.mark.asyncio
async def test_users_get_id_361458326017907882():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'requestId': '7157g2pa8mmw4hrhmhw', 'user': {'id': '361458326017907882', 'emailAddress': 'integration-test@airbyte.io', 'created': '2022-11-29T16:21:34.192+02:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'Airbyte', 'lastName': 'Team', 'title': None, 'phoneNumber': '+14156236785', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.users.get(id="361458326017907882")

    assert result == mock_response


@pytest.mark.asyncio
async def test_users_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'requestId': '4jryhg4awrdhb6bc3jx', 'records': {'totalRecords': 9, 'currentPageSize': 9, 'currentPageNumber': 0}, 'users': [{'id': '361458326017907882', 'emailAddress': 'integration-test@airbyte.io', 'created': '2022-11-29T16:21:34.192+02:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'Airbyte', 'lastName': 'Team', 'title': None, 'phoneNumber': '+14156236785', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}, {'id': '2004171275038585911', 'emailAddress': 'user8.sample.airbyte@outlook.com', 'created': '2023-04-11T14:16:12.337+03:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'User8', 'lastName': 'Sample', 'title': None, 'phoneNumber': '+13335556789', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}, {'id': '2481630679109750242', 'emailAddress': 'user2.sample.airbyte@gmail.com', 'created': '2023-04-11T13:06:56.389+03:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'User2', 'lastName': 'Sample', 'title': None, 'phoneNumber': '+13335556789', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}, {'id': '4601305870033665258', 'emailAddress': 'user4.sample.airbyte@outlook.com', 'created': '2023-04-11T14:09:32.245+03:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'User4', 'lastName': 'Sample', 'title': None, 'phoneNumber': '+13335556789', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}, {'id': '4642729273019511289', 'emailAddress': 'user6.sample.airbyte@outlook.com', 'created': '2023-04-11T14:15:22.691+03:00', 'active': True, 'emailAliases': ['user7.sample.airbyte@outlook.com'], 'trustedEmailAddress': None, 'firstName': 'User5', 'lastName': 'Sample', 'title': 'Developer', 'phoneNumber': '+13335556789', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': '2481630679109750242', 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}, {'id': '4873306101987630010', 'emailAddress': 'user1.sample@zohomail.eu', 'created': '2023-04-11T13:05:09.371+03:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'User1', 'lastName': 'Sample', 'title': None, 'phoneNumber': None, 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}, {'id': '5006202833642160293', 'emailAddress': 'user9.sample.airbyte@outlook.com', 'created': '2023-04-11T14:16:36.041+03:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'User9', 'lastName': 'Sample', 'title': None, 'phoneNumber': '+13335556789', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': []}, {'id': '6197867528524620585', 'emailAddress': 'user10.sample.airbyte@outlook.com', 'created': '2023-04-11T14:16:54.903+03:00', 'active': True, 'emailAliases': [], 'trustedEmailAddress': None, 'firstName': 'User10', 'lastName': 'Sample', 'title': None, 'phoneNumber': '+13335556789', 'extension': None, 'personalMeetingUrls': [], 'settings': {'webConferencesRecorded': False, 'preventWebConferenceRecording': False, 'telephonyCallsImported': False, 'emailsImported': False, 'preventEmailImport': False, 'nonRecordedMeetingsImported': False, 'gongConnectEnabled': False}, 'managerId': None, 'meetingConsentPageUrl': None, 'spokenLanguages': []}, {'id': '7584086951822993456', 'emailAddress': 'user3.sample.airbyte@outlook.com', 'created': '2023-04-11T13:09:29.333+03:00', 'active': True, 'emailAliases': ['user5.sample.airbyte@outlook.com'], 'trustedEmailAddress': None, 'firstName': 'User3', 'lastName': 'Sample', 'title': 'Test', 'phoneNumber': '+13335556789', 'extension': '333', 'personalMeetingUrls': ['https://meet.google.com/qtv-veys-kkz'], 'settings': {'webConferencesRecorded': True, 'preventWebConferenceRecording': False, 'telephonyCallsImported': True, 'emailsImported': True, 'preventEmailImport': False, 'nonRecordedMeetingsImported': True, 'gongConnectEnabled': True}, 'managerId': '361458326017907882', 'meetingConsentPageUrl': None, 'spokenLanguages': [{'language': 'en-US', 'primary': True}]}]}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.users.list()

    assert result == mock_response


@pytest.mark.asyncio
async def test_workspaces_list():
    """Captured from real API call on 2025-11-20"""
    mock_response = {'requestId': 'e18ayw9wum5j14ljp9', 'workspaces': [{'id': '9196197544788600771', 'name': 'Initial workspace', 'description': 'The built-in workspace'}]}

    connector = GongConnector.create(secrets={"username": "test_key", "password": "test_key"})

    with patch(
        "airbyte_ai_gong._vendored.connector_sdk.http_client.HTTPClient.request",
        new=AsyncMock(return_value=mock_response)
    ):
        result = await connector.workspaces.list()

    assert result == mock_response

