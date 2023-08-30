# https://github.com/opensearch-project/OpenSearch/blob/main/server/src/main/java/org/opensearch/transport/NetworkMessage.java

from opensearch_sdk_py.transport.tcp_header import TcpHeader
from opensearch_sdk_py.transport.thread_context_struct import ThreadContextStruct
from opensearch_sdk_py.transport.version import Version

class NetworkMessage():
    def __init__(self, thread_context: ThreadContextStruct=None, version: Version=None, status: int=0, request_id: int=1):
        self.thread_context_struct = thread_context if thread_context else ThreadContextStruct()
        self.tcp_header = TcpHeader(version=version, status=status, request_id=request_id)

    def get_version(self) -> Version:
        return self.tcp_header.version
    
    def get_request_id(self) -> int:
        return self.tcp_header.request_id

    def is_request(self) -> bool:
        return self.tcp_header.is_request()

    def is_response(self) -> bool:
        return self.tcp_header.is_request() == False

    def is_error(self) -> bool:
        return self.tcp_header.is_error()

    def is_compress(self) -> bool:
        return self.tcp_header.is_compress()

    def is_handshake(self) -> bool:
        return self.tcp_header.is_handshake()
