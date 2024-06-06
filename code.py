from pprint import pprint

from VideoIndexerClient.Consts import Consts
from VideoIndexerClient.VideoIndexerClient import VideoIndexerClient


#config = dotenv_values(".env")

AccountName = 'demo-aivideindexer'
ResourceGroup = 'demo-res'
SubscriptionId = '113b1fed-e329-464a-a730-82128f02030d'

ApiVersion = '2024-01-01'
ApiEndpoint = 'https://api.videoindexer.ai'
AzureResourceManager = 'https://management.azure.com'

# create and validate consts
consts = Consts(ApiVersion, ApiEndpoint, AzureResourceManager, AccountName, ResourceGroup, SubscriptionId)


# create Video Indexer Client
client = VideoIndexerClient()

# Get access tokens (arm and Video Indexer account)
client.authenticate_async(consts)


client.get_account_async()

VideoUrl = 'https://demoacostastorage.blob.core.windows.net/files/molotov_interview.mp4'
ExcludedAI = []

video_id = client.upload_url_async('my-video-name', VideoUrl, ExcludedAI, False)

client.wait_for_index_async(video_id)

insights = client.get_video_async(video_id)
pprint(insights)