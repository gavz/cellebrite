"""
    Base Chain
    The class defines the basic structure for Chain object,
    Which may contains framers, protocols, dumpers, and uploaders.
    Chain should retreive an initialized connection object

    Written by NirZ
    12/08/10
"""
from Mits.Framers.FramerRETeam                  import FramerRETeam
from Mits.Protocols.ProtocolRETeam              import ProtocolRETeam
from Mits.Dumpers.DumperRam                     import DumperRam
from Mits.Dumpers.DumperNand                    import DumperNand
from Mits.Dumpers.DumperOneNand                 import DumperOneNand
from Mits.Dumpers.DumperMMC                 import DumperMMC


class BaseChain:
    def __init__(self, name, conn, safe_recv = False):
        self.conn = conn
        self.safe_recv = safe_recv
        self.framers     = {}
        self.protocols   = {}
        self.dumpers     = {}
        self.uploaders   = {}
        self.__name      = name

        self.__init_default_chain()

    def __init_default_chain(self, base_framer = None):
        """all you need to communicate with the bootloader"""
        if (None == base_framer):
            self.framers[FramerRETeam.name]         = FramerRETeam(self.conn)
        else:
            self.framers[FramerRETeam.name]         = FramerRETeam(base_framer)
        self.protocols[ProtocolRETeam.name]     = ProtocolRETeam(self.framers[FramerRETeam.name], safe_recv = self.safe_recv)
        self.dumpers[DumperRam.name]            = DumperRam(self.protocols[ProtocolRETeam.name])
        self.dumpers[DumperNand.name]           = DumperNand(self.protocols[ProtocolRETeam.name])
        self.dumpers[DumperOneNand.name]        = DumperOneNand(self.protocols[ProtocolRETeam.name])
        self.dumpers[DumperMMC.name]            = DumperMMC(self.protocols[ProtocolRETeam.name])

    def __dic_repr(self, title, dic):
        txt = ""
        if (len(dic.keys()) > 0):
            txt += title + ":" + "\r\n"
            txt += "".join(["\t"+key + "\r\n"for key in dic.keys()])
            txt +=  "-" * 40 + "\r\n"
        return txt


    def __repr__(self):
        txt = "Chain: " + self.__name + "\r\n"
        txt += self.__dic_repr("Framers",  self.framers)
        txt += self.__dic_repr("Protocols",  self.protocols)
        txt += self.__dic_repr("Uploaders",  self.uploaders)
        txt += self.__dic_repr("Dumpers",  self.dumpers)

        return txt

    def close(self):
        self.conn.close()

    def connect(self):
        self.conn.connect()
