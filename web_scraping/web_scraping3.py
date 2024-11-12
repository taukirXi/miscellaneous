from urllib.parse import urlparse

# library: urllib module is urlparse


def withUrlparse():

    url1 = "https://docs.python.org/3/"
    url2 = "https://www.google.com/search?q=glendalough+deer+times&oq=glendalough+deer+times&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRifBTIHCAQQIRiPAtIBCTExNTc5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8"
    try:
        result = urlparse(url2)
        print(result)
    except:
        print('An exception occurred')


withUrlparse()
