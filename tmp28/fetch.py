import json,urllib.request,urllib.parse,sys
UA={'User-Agent':'history-timeline-builder/1.0 (https://github.com/krielherman8-source/history-timeline)'}
T=[l.strip() for l in open(sys.argv[1]) if l.strip()]
for t in T:
  u='https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts|pageimages&piprop=name&exintro=1&explaintext=1&redirects=1&titles='+urllib.parse.quote(t)
  try:
    p=list(json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30))['query']['pages'].values())[0]
    print('=====',t,'->',p.get('title'),'| img:',p.get('pageimage'),'| missing' if 'missing' in p else '')
    print((p.get('extract') or '')[:2200])
  except Exception as e: print('=====',t,'ERR',e)
