from PMS import Plugin, Log, DB, Thread, XML, HTTP, JSON, RSS, Utils
from PMS.MediaXML import MediaContainer, DirectoryItem, PhotoItem

PLUGIN_PREFIX   = "/photos/PhotoShoq"
RSS_FEED        = "http://photo.shoq.com/index.php?PageID=108"

####################################################################################################
def Start():
  Plugin.AddRequestHandler(PLUGIN_PREFIX, HandlePhotosRequest, "Photo.Shoq", "icon-default.png", "art-default.png")
  Plugin.AddViewGroup("Pictures", viewMode="InfoList", contentType="photos")

####################################################################################################
def HandlePhotosRequest(pathNouns, count):
  dir = MediaContainer("art-default.png", "Pictures", "Photo.Shoq")
  
  if count == 0:
    for item in RSS.Parse(RSS_FEED).entries:
      node = XML.ElementFromString(item.content[0].value, True)
      summary = ' '.join(node.xpath("//text()")).replace('\n','').strip()
      img = node.xpath("//img")[0].get('src')
      dir.AppendItem(PhotoItem(img, item.title, summary, img))

  return dir.ToXML()
