from passlib.context import CryptContext

psw_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



def hashed_psw(psw : str):
    hashed = psw_context.hash(psw)
    return hashed

def verify_psw(plain_psw: str, hashed_psw : str):
    verify = psw_context.verify(plain_psw, hashed_psw)
    return verify