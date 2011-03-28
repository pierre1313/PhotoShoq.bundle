PLUGIN_PREFIX   = "/photos/PhotoShoq"
#RSS_FEED        = "http://photo.shoq.com/index.php?PageID=108"
RSS_FEED        = "http://jaspervandermeij.nl/feed/"

####################################################################################################
def Start():
  Plugin.AddPrefixHandler(PLUGIN_PREFIX, MainMenu, "Photo.Shoq", "icon-default.png", "art-default.png")
  Plugin.AddViewGroup("Pictures", viewMode="InfoList", mediaType="photos")

####################################################################################################
def MainMenu():
  dir = MediaContainer(art=R("art-default.png"), viewGroup ="Pictures", title1="Photo.Shoq")
  
  for item in RSS.FeedFromURL(RSS_FEED).entries:
    node = HTML.ElementFromString(item.content[0].value)
    summary = ' '.join(node.xpath("//text()")).replace('\n','').strip()
    img = node.xpath("//img")[0].get('src')
    dir.Append(PhotoItem(img, item.title, summary, img))

  return dir
