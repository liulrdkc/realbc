import binascii

class Digest(bytes):
    @classmethod
    def zero(cls)->'Digest':
        return cls(32)
        
    def __repr__(self) -> str:
        return binascii.hexlify(self).decode('ascii')
        
    @classmethod
    def sha256(*var)->Digest:
        ctx = hashlib.sha256()
        for val in vals:
            if isinstance(val, str):
                ctx.update(val.encode('utf8'))
            elif isinstance(val, int):
                ctx.update(val.to_bytes(16, 'big'))
            elif hasattr(val, '__digest__'):
                ctx.update(val.__digest__())
            else:
                ctx.update(val)
        return Digest(ctx.digest())
