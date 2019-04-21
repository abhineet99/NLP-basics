from warcio.archiveiterator import ArchiveIterator
nytimes="nytimes"
with open('CC-NEWS-20190314221726-00599.warc.gz', 'rb') as stream:
    for record in ArchiveIterator(stream):
        if record.rec_type == 'response':
            if record.rec_headers.get_header('WARC-Target-URI')[12:19] == nytimes:
                print(record.rec_headers.get_header('WARC-Target-URI'))
                #print(record.content_stream().read())
            #print(record.http_headers.get_header('Content-Language'))
		
