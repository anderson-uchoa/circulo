from src.aluno.g_contatos import GContatos

if __name__ == '__main__':
    AMIGOS = "amigos"
    TRABALHO = "trabalho"
    FAMILIA = "familia"
    JOAQUIM_EMAIL = "joaquim@ufc.br"
    JOAQUIM = "joaquim"
    ANA_EMAIL = "ana@ufc.br"
    ANA = "ana"
    MARIO_EMAIL = "mario@ufc.br"
    MARIO = "mario"
    JOSE_EMAIL = "jose@ufc.br"
    JOSE = "jose"
    JAMES_EMAIL = "james@ufc.com"
    JAMES = "james"

    gcont = GContatos()

    gcont.createCircle(FAMILIA, 3)
    gcont.createCircle(AMIGOS, 2)
    gcont.createCircle(TRABALHO, 3)
    print(gcont.getAllCircles())

    gcont.createContact(JAMES, JAMES_EMAIL)
    gcont.createContact(MARIO, MARIO_EMAIL)
    gcont.createContact(JOSE, JOSE_EMAIL)
    gcont.createContact(ANA, ANA_EMAIL)
    gcont.createContact(JOAQUIM, JOAQUIM_EMAIL)
    print(gcont.getAllContacts())

    gcont.tie(MARIO, FAMILIA)
    print(gcont.getCircles(MARIO))

    gcont.tie(JAMES, TRABALHO)
    gcont.tie(JOAQUIM, TRABALHO)
    gcont.tie(ANA, TRABALHO)
    print(gcont.getContacts(TRABALHO))

    gcont.tie(JAMES, AMIGOS)
    gcont.tie(MARIO, AMIGOS)
    print(gcont.getContacts(AMIGOS))

    print(gcont.getCommomCircle(JAMES, ANA))
    print(gcont.getCommomCircle(JAMES, JOSE))
    print(gcont.getCommomCircle(JAMES, MARIO))

