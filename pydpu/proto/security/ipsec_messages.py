# AUTO-GENERATED CODE - DO NOT MODIFY
# Modifications may be overwritten during future updates

from typing import List
from enum import Enum

class IntegAlgorithm(Enum):
        INTEG_ALGORITHM_UNSPECIFIED = 0
        INTEG_ALGORITHM_MD5 = 1
        INTEG_ALGORITHM_MD5_128 = 2
        INTEG_ALGORITHM_SHA1 = 3
        INTEG_ALGORITHM_SHA1_160 = 4
        INTEG_ALGORITHM_SHA256 = 5
        INTEG_ALGORITHM_SHA384 = 7
        INTEG_ALGORITHM_SHA512 = 8
        INTEG_ALGORITHM_SHA256_96 = 9


class CryptoAlgorithm(Enum):
        CRYPTO_ALGORITHM_UNSPECIFIED = 0
        CRYPTO_ALGORITHM_AES128 = 1
        CRYPTO_ALGORITHM_AES192 = 2
        CRYPTO_ALGORITHM_AES256 = 3
        CRYPTO_ALGORITHM_AES128GCM128 = 4
        CRYPTO_ALGORITHM_AES256GCM128 = 5
        CRYPTO_ALGORITHM_AES128GMAC = 6
        CRYPTO_ALGORITHM_AES256GMAC = 7


class DHGroups(Enum):
        DH_GROUPS_UNSPECIFIED = 0
        DH_GROUPS_MODP768 = 1
        DH_GROUPS_MODP1024 = 2
        DH_GROUPS_MODP1536 = 3
        DH_GROUPS_MODP2048 = 4
        DH_GROUPS_MODP3072 = 5
        DH_GROUPS_MODP4096 = 6
        DH_GROUPS_MODP6144 = 7
        DH_GROUPS_MODP8192 = 8
        DH_GROUPS_MODP1024S160 = 9
        DH_GROUPS_MODP2048S224 = 10
        DH_GROUPS_MODP2048S256 = 11
        DH_GROUPS_CURVE25519 = 12


class PRFunction(Enum):
        PR_FUNCTION_UNSPECIFIED = 0
        PR_FUNCTION_MD5 = 1
        PR_FUNCTION_SHA1 = 2
        PR_FUNCTION_AESXCBC = 3
        PR_FUNCTION_AESCMAC = 4
        PR_FUNCTION_SHA256 = 5
        PR_FUNCTION_SHA384 = 6
        PR_FUNCTION_SHA512 = 7


class TrafficSelector:

    def __init__(self, cidr, port, proto):
        _cidr = cidr
        _port = port
        _proto = proto

        
    @property
    def cidr(self) -> str:
        return self._cidr

    @cidr.setter
    def cidr(self, value: str):
        self._cidr = value

        
    @property
    def port(self) -> str:
        return self._port

    @port.setter
    def port(self, value: str):
        self._port = value

        
    @property
    def proto(self) -> str:
        return self._proto

    @proto.setter
    def proto(self, value: str):
        self._proto = value



class Proposals:

    def __init__(self, integ_alg, crypto_alg, prf, dhgroups):
        _integ_alg = integ_alg
        _crypto_alg = crypto_alg
        _prf = prf
        _dhgroups = dhgroups

        
    @property
    def integ_alg(self) -> List[Enum]:
        return self._integ_alg

    @integ_alg.setter
    def integ_alg(self, value: List[Enum]):
        self._integ_alg = value

        
    @property
    def crypto_alg(self) -> List[Enum]:
        return self._crypto_alg

    @crypto_alg.setter
    def crypto_alg(self, value: List[Enum]):
        self._crypto_alg = value

        
    @property
    def prf(self) -> List[Enum]:
        return self._prf

    @prf.setter
    def prf(self, value: List[Enum]):
        self._prf = value

        
    @property
    def dhgroups(self) -> List[Enum]:
        return self._dhgroups

    @dhgroups.setter
    def dhgroups(self, value: List[Enum]):
        self._dhgroups = value



class TrafficSelectors:

    def __init__(self, ts):
        _ts = ts

        
    @property
    def ts(self) -> List[TrafficSelector]:
        return self._ts

    @ts.setter
    def ts(self, value: List[TrafficSelector]):
        self._ts = value



class PubKeys:

    def __init__(self, pubkey):
        _pubkey = pubkey

        
    @property
    def pubkey(self) -> List[str]:
        return self._pubkey

    @pubkey.setter
    def pubkey(self, value: List[str]):
        self._pubkey = value



class CertPolicy:

    def __init__(self, cert_policy):
        _cert_policy = cert_policy

        
    @property
    def cert_policy(self) -> List[str]:
        return self._cert_policy

    @cert_policy.setter
    def cert_policy(self, value: List[str]):
        self._cert_policy = value



class Groups:

    def __init__(self, group):
        _group = group

        
    @property
    def group(self) -> List[str]:
        return self._group

    @group.setter
    def group(self, value: List[str]):
        self._group = value



class Certs:

    def __init__(self, cert):
        _cert = cert

        
    @property
    def cert(self) -> List[str]:
        return self._cert

    @cert.setter
    def cert(self, value: List[str]):
        self._cert = value



class CaCerts:

    def __init__(self, cacert):
        _cacert = cacert

        
    @property
    def cacert(self) -> List[str]:
        return self._cacert

    @cacert.setter
    def cacert(self, value: List[str]):
        self._cacert = value



class Child:
    """ Child SA """
    def __init__(self, inactivity, mark_out, local_ts, ag_proposals, name, remote_ts, updown, rand_time, hw_offload, mark_in, set_mark_in, set_mark_out, life_time, mark_in_sa, rekey_time, esp_proposals):
        _inactivity = inactivity
        _mark_out = mark_out
        _local_ts = local_ts
        _ag_proposals = ag_proposals
        _name = name
        _remote_ts = remote_ts
        _updown = updown
        _rand_time = rand_time
        _hw_offload = hw_offload
        _mark_in = mark_in
        _set_mark_in = set_mark_in
        _set_mark_out = set_mark_out
        _life_time = life_time
        _mark_in_sa = mark_in_sa
        _rekey_time = rekey_time
        _esp_proposals = esp_proposals

        
    @property
    def inactivity(self) -> None:
        return self._inactivity

    @inactivity.setter
    def inactivity(self, value: None):
        self._inactivity = value

        
    @property
    def mark_out(self) -> None:
        return self._mark_out

    @mark_out.setter
    def mark_out(self, value: None):
        self._mark_out = value

        
    @property
    def local_ts(self) -> TrafficSelectors:
        return self._local_ts

    @local_ts.setter
    def local_ts(self, value: TrafficSelectors):
        self._local_ts = value

        
    @property
    def ag_proposals(self) -> Proposals:
        return self._ag_proposals

    @ag_proposals.setter
    def ag_proposals(self, value: Proposals):
        self._ag_proposals = value

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

        
    @property
    def remote_ts(self) -> TrafficSelectors:
        return self._remote_ts

    @remote_ts.setter
    def remote_ts(self, value: TrafficSelectors):
        self._remote_ts = value

        
    @property
    def updown(self) -> str:
        return self._updown

    @updown.setter
    def updown(self, value: str):
        self._updown = value

        
    @property
    def rand_time(self) -> None:
        return self._rand_time

    @rand_time.setter
    def rand_time(self, value: None):
        self._rand_time = value

        
    @property
    def hw_offload(self) -> str:
        return self._hw_offload

    @hw_offload.setter
    def hw_offload(self, value: str):
        self._hw_offload = value

        
    @property
    def mark_in(self) -> None:
        return self._mark_in

    @mark_in.setter
    def mark_in(self, value: None):
        self._mark_in = value

        
    @property
    def set_mark_in(self) -> None:
        return self._set_mark_in

    @set_mark_in.setter
    def set_mark_in(self, value: None):
        self._set_mark_in = value

        
    @property
    def set_mark_out(self) -> None:
        return self._set_mark_out

    @set_mark_out.setter
    def set_mark_out(self, value: None):
        self._set_mark_out = value

        
    @property
    def life_time(self) -> None:
        return self._life_time

    @life_time.setter
    def life_time(self, value: None):
        self._life_time = value

        
    @property
    def mark_in_sa(self) -> str:
        return self._mark_in_sa

    @mark_in_sa.setter
    def mark_in_sa(self, value: str):
        self._mark_in_sa = value

        
    @property
    def rekey_time(self) -> None:
        return self._rekey_time

    @rekey_time.setter
    def rekey_time(self, value: None):
        self._rekey_time = value

        
    @property
    def esp_proposals(self) -> Proposals:
        return self._esp_proposals

    @esp_proposals.setter
    def esp_proposals(self, value: Proposals):
        self._esp_proposals = value



class RemoteAuth:

    def __init__(self, eap_id, auth, ca_certs, certs, groups, cert_policy, pubkeys, id):
        _eap_id = eap_id
        _auth = auth
        _ca_certs = ca_certs
        _certs = certs
        _groups = groups
        _cert_policy = cert_policy
        _pubkeys = pubkeys
        _id = id

        
    @property
    def eap_id(self) -> str:
        return self._eap_id

    @eap_id.setter
    def eap_id(self, value: str):
        self._eap_id = value

        
    @property
    def auth(self) -> None:
        return self._auth

    @auth.setter
    def auth(self, value: None):
        self._auth = value

        
    @property
    def ca_certs(self) -> CaCerts:
        return self._ca_certs

    @ca_certs.setter
    def ca_certs(self, value: CaCerts):
        self._ca_certs = value

        
    @property
    def certs(self) -> Certs:
        return self._certs

    @certs.setter
    def certs(self, value: Certs):
        self._certs = value

        
    @property
    def groups(self) -> Groups:
        return self._groups

    @groups.setter
    def groups(self, value: Groups):
        self._groups = value

        
    @property
    def cert_policy(self) -> CertPolicy:
        return self._cert_policy

    @cert_policy.setter
    def cert_policy(self, value: CertPolicy):
        self._cert_policy = value

        
    @property
    def pubkeys(self) -> PubKeys:
        return self._pubkeys

    @pubkeys.setter
    def pubkeys(self, value: PubKeys):
        self._pubkeys = value

        
    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value



class Addrs:
    """ IP addresses or hostanmes """
    def __init__(self, addr):
        _addr = addr

        
    @property
    def addr(self) -> str:
        return self._addr

    @addr.setter
    def addr(self, value: str):
        self._addr = value



class Pools:

    def __init__(self, pool):
        _pool = pool

        
    @property
    def pool(self) -> List[str]:
        return self._pool

    @pool.setter
    def pool(self, value: List[str]):
        self._pool = value



class LocalAuth:

    def __init__(self, aaa_id, eap_id, auth, certs, xauth_id, pubkeys, id):
        _aaa_id = aaa_id
        _eap_id = eap_id
        _auth = auth
        _certs = certs
        _xauth_id = xauth_id
        _pubkeys = pubkeys
        _id = id

        
    @property
    def aaa_id(self) -> str:
        return self._aaa_id

    @aaa_id.setter
    def aaa_id(self, value: str):
        self._aaa_id = value

        
    @property
    def eap_id(self) -> str:
        return self._eap_id

    @eap_id.setter
    def eap_id(self, value: str):
        self._eap_id = value

        
    @property
    def auth(self) -> None:
        return self._auth

    @auth.setter
    def auth(self, value: None):
        self._auth = value

        
    @property
    def certs(self) -> Certs:
        return self._certs

    @certs.setter
    def certs(self, value: Certs):
        self._certs = value

        
    @property
    def xauth_id(self) -> str:
        return self._xauth_id

    @xauth_id.setter
    def xauth_id(self, value: str):
        self._xauth_id = value

        
    @property
    def pubkeys(self) -> PubKeys:
        return self._pubkeys

    @pubkeys.setter
    def pubkeys(self, value: PubKeys):
        self._pubkeys = value

        
    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value



class Vips:

    def __init__(self, vip):
        _vip = vip

        
    @property
    def vip(self) -> List[str]:
        return self._vip

    @vip.setter
    def vip(self, value: List[str]):
        self._vip = value



class ListChild:

    def __init__(self, local_ts, name, rekey_packets, remote_ts, label, priority, mode, dpd_action, interface, close_action, rekey_time, rekey_bytes):
        _local_ts = local_ts
        _name = name
        _rekey_packets = rekey_packets
        _remote_ts = remote_ts
        _label = label
        _priority = priority
        _mode = mode
        _dpd_action = dpd_action
        _interface = interface
        _close_action = close_action
        _rekey_time = rekey_time
        _rekey_bytes = rekey_bytes

        
    @property
    def local_ts(self) -> TrafficSelectors:
        return self._local_ts

    @local_ts.setter
    def local_ts(self, value: TrafficSelectors):
        self._local_ts = value

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

        
    @property
    def rekey_packets(self) -> None:
        return self._rekey_packets

    @rekey_packets.setter
    def rekey_packets(self, value: None):
        self._rekey_packets = value

        
    @property
    def remote_ts(self) -> TrafficSelectors:
        return self._remote_ts

    @remote_ts.setter
    def remote_ts(self, value: TrafficSelectors):
        self._remote_ts = value

        
    @property
    def label(self) -> str:
        return self._label

    @label.setter
    def label(self, value: str):
        self._label = value

        
    @property
    def priority(self) -> str:
        return self._priority

    @priority.setter
    def priority(self, value: str):
        self._priority = value

        
    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, value: str):
        self._mode = value

        
    @property
    def dpd_action(self) -> str:
        return self._dpd_action

    @dpd_action.setter
    def dpd_action(self, value: str):
        self._dpd_action = value

        
    @property
    def interface(self) -> str:
        return self._interface

    @interface.setter
    def interface(self, value: str):
        self._interface = value

        
    @property
    def close_action(self) -> str:
        return self._close_action

    @close_action.setter
    def close_action(self, value: str):
        self._close_action = value

        
    @property
    def rekey_time(self) -> None:
        return self._rekey_time

    @rekey_time.setter
    def rekey_time(self, value: None):
        self._rekey_time = value

        
    @property
    def rekey_bytes(self) -> None:
        return self._rekey_bytes

    @rekey_bytes.setter
    def rekey_bytes(self, value: None):
        self._rekey_bytes = value



class ListConnAuth:

    def __init__(self, group, revocation, aaa_id, eap_id, eapvendor, cacerts, class, certs, ca_id, xauth, cert_policy, xauth_id, eaptype, id):
        _group = group
        _revocation = revocation
        _aaa_id = aaa_id
        _eap_id = eap_id
        _eapvendor = eapvendor
        _cacerts = cacerts
        _class = class
        _certs = certs
        _ca_id = ca_id
        _xauth = xauth
        _cert_policy = cert_policy
        _xauth_id = xauth_id
        _eaptype = eaptype
        _id = id

        
    @property
    def group(self) -> Groups:
        return self._group

    @group.setter
    def group(self, value: Groups):
        self._group = value

        
    @property
    def revocation(self) -> str:
        return self._revocation

    @revocation.setter
    def revocation(self, value: str):
        self._revocation = value

        
    @property
    def aaa_id(self) -> str:
        return self._aaa_id

    @aaa_id.setter
    def aaa_id(self, value: str):
        self._aaa_id = value

        
    @property
    def eap_id(self) -> str:
        return self._eap_id

    @eap_id.setter
    def eap_id(self, value: str):
        self._eap_id = value

        
    @property
    def eapvendor(self) -> str:
        return self._eapvendor

    @eapvendor.setter
    def eapvendor(self, value: str):
        self._eapvendor = value

        
    @property
    def cacerts(self) -> CaCerts:
        return self._cacerts

    @cacerts.setter
    def cacerts(self, value: CaCerts):
        self._cacerts = value

        
    @property
    def class(self) -> str:
        return self._class

    @class.setter
    def class(self, value: str):
        self._class = value

        
    @property
    def certs(self) -> Certs:
        return self._certs

    @certs.setter
    def certs(self, value: Certs):
        self._certs = value

        
    @property
    def ca_id(self) -> str:
        return self._ca_id

    @ca_id.setter
    def ca_id(self, value: str):
        self._ca_id = value

        
    @property
    def xauth(self) -> str:
        return self._xauth

    @xauth.setter
    def xauth(self, value: str):
        self._xauth = value

        
    @property
    def cert_policy(self) -> CertPolicy:
        return self._cert_policy

    @cert_policy.setter
    def cert_policy(self, value: CertPolicy):
        self._cert_policy = value

        
    @property
    def xauth_id(self) -> str:
        return self._xauth_id

    @xauth_id.setter
    def xauth_id(self, value: str):
        self._xauth_id = value

        
    @property
    def eaptype(self) -> str:
        return self._eaptype

    @eaptype.setter
    def eaptype(self, value: str):
        self._eaptype = value

        
    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, value: str):
        self._id = value



class ListChildSa:

    def __init__(self, mark_out, protocol, name, spi_out, encr_alg, integ_keysize, cpi_in, encr_keysize, mark_in, mark_mask_in, if_id_in, mark_mask_out, encap, esn, cpi_out, integ_alg, dh_group, spi_in, if_id_out):
        _mark_out = mark_out
        _protocol = protocol
        _name = name
        _spi_out = spi_out
        _encr_alg = encr_alg
        _integ_keysize = integ_keysize
        _cpi_in = cpi_in
        _encr_keysize = encr_keysize
        _mark_in = mark_in
        _mark_mask_in = mark_mask_in
        _if_id_in = if_id_in
        _mark_mask_out = mark_mask_out
        _encap = encap
        _esn = esn
        _cpi_out = cpi_out
        _integ_alg = integ_alg
        _dh_group = dh_group
        _spi_in = spi_in
        _if_id_out = if_id_out

        
    @property
    def mark_out(self) -> str:
        return self._mark_out

    @mark_out.setter
    def mark_out(self, value: str):
        self._mark_out = value

        
    @property
    def protocol(self) -> str:
        return self._protocol

    @protocol.setter
    def protocol(self, value: str):
        self._protocol = value

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

        
    @property
    def spi_out(self) -> str:
        return self._spi_out

    @spi_out.setter
    def spi_out(self, value: str):
        self._spi_out = value

        
    @property
    def encr_alg(self) -> str:
        return self._encr_alg

    @encr_alg.setter
    def encr_alg(self, value: str):
        self._encr_alg = value

        
    @property
    def integ_keysize(self) -> str:
        return self._integ_keysize

    @integ_keysize.setter
    def integ_keysize(self, value: str):
        self._integ_keysize = value

        
    @property
    def cpi_in(self) -> str:
        return self._cpi_in

    @cpi_in.setter
    def cpi_in(self, value: str):
        self._cpi_in = value

        
    @property
    def encr_keysize(self) -> str:
        return self._encr_keysize

    @encr_keysize.setter
    def encr_keysize(self, value: str):
        self._encr_keysize = value

        
    @property
    def mark_in(self) -> str:
        return self._mark_in

    @mark_in.setter
    def mark_in(self, value: str):
        self._mark_in = value

        
    @property
    def mark_mask_in(self) -> str:
        return self._mark_mask_in

    @mark_mask_in.setter
    def mark_mask_in(self, value: str):
        self._mark_mask_in = value

        
    @property
    def if_id_in(self) -> str:
        return self._if_id_in

    @if_id_in.setter
    def if_id_in(self, value: str):
        self._if_id_in = value

        
    @property
    def mark_mask_out(self) -> str:
        return self._mark_mask_out

    @mark_mask_out.setter
    def mark_mask_out(self, value: str):
        self._mark_mask_out = value

        
    @property
    def encap(self) -> str:
        return self._encap

    @encap.setter
    def encap(self, value: str):
        self._encap = value

        
    @property
    def esn(self) -> str:
        return self._esn

    @esn.setter
    def esn(self, value: str):
        self._esn = value

        
    @property
    def cpi_out(self) -> str:
        return self._cpi_out

    @cpi_out.setter
    def cpi_out(self, value: str):
        self._cpi_out = value

        
    @property
    def integ_alg(self) -> str:
        return self._integ_alg

    @integ_alg.setter
    def integ_alg(self, value: str):
        self._integ_alg = value

        
    @property
    def dh_group(self) -> str:
        return self._dh_group

    @dh_group.setter
    def dh_group(self, value: str):
        self._dh_group = value

        
    @property
    def spi_in(self) -> str:
        return self._spi_in

    @spi_in.setter
    def spi_in(self, value: str):
        self._spi_in = value

        
    @property
    def if_id_out(self) -> str:
        return self._if_id_out

    @if_id_out.setter
    def if_id_out(self, value: str):
        self._if_id_out = value



class Connection:
    """ IKE connection """
    def __init__(self, dpd_timeout, vips, name, local_port, reauth_time, remote_port, proposals, dscp, dpd_delay, version, local_auth, encap, local_addrs, pools, mobike, remote_addrs, remote_auth, children, rekey_time):
        _dpd_timeout = dpd_timeout
        _vips = vips
        _name = name
        _local_port = local_port
        _reauth_time = reauth_time
        _remote_port = remote_port
        _proposals = proposals
        _dscp = dscp
        _dpd_delay = dpd_delay
        _version = version
        _local_auth = local_auth
        _encap = encap
        _local_addrs = local_addrs
        _pools = pools
        _mobike = mobike
        _remote_addrs = remote_addrs
        _remote_auth = remote_auth
        _children = children
        _rekey_time = rekey_time

        
    @property
    def dpd_timeout(self) -> None:
        return self._dpd_timeout

    @dpd_timeout.setter
    def dpd_timeout(self, value: None):
        self._dpd_timeout = value

        
    @property
    def vips(self) -> Vips:
        return self._vips

    @vips.setter
    def vips(self, value: Vips):
        self._vips = value

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

        
    @property
    def local_port(self) -> None:
        return self._local_port

    @local_port.setter
    def local_port(self, value: None):
        self._local_port = value

        
    @property
    def reauth_time(self) -> None:
        return self._reauth_time

    @reauth_time.setter
    def reauth_time(self, value: None):
        self._reauth_time = value

        
    @property
    def remote_port(self) -> None:
        return self._remote_port

    @remote_port.setter
    def remote_port(self, value: None):
        self._remote_port = value

        
    @property
    def proposals(self) -> Proposals:
        return self._proposals

    @proposals.setter
    def proposals(self, value: Proposals):
        self._proposals = value

        
    @property
    def dscp(self) -> str:
        return self._dscp

    @dscp.setter
    def dscp(self, value: str):
        self._dscp = value

        
    @property
    def dpd_delay(self) -> None:
        return self._dpd_delay

    @dpd_delay.setter
    def dpd_delay(self, value: None):
        self._dpd_delay = value

        
    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

        
    @property
    def local_auth(self) -> LocalAuth:
        return self._local_auth

    @local_auth.setter
    def local_auth(self, value: LocalAuth):
        self._local_auth = value

        
    @property
    def encap(self) -> str:
        return self._encap

    @encap.setter
    def encap(self, value: str):
        self._encap = value

        
    @property
    def local_addrs(self) -> List[Addrs]:
        return self._local_addrs

    @local_addrs.setter
    def local_addrs(self, value: List[Addrs]):
        self._local_addrs = value

        
    @property
    def pools(self) -> Pools:
        return self._pools

    @pools.setter
    def pools(self, value: Pools):
        self._pools = value

        
    @property
    def mobike(self) -> str:
        return self._mobike

    @mobike.setter
    def mobike(self, value: str):
        self._mobike = value

        
    @property
    def remote_addrs(self) -> List[Addrs]:
        return self._remote_addrs

    @remote_addrs.setter
    def remote_addrs(self, value: List[Addrs]):
        self._remote_addrs = value

        
    @property
    def remote_auth(self) -> RemoteAuth:
        return self._remote_auth

    @remote_auth.setter
    def remote_auth(self, value: RemoteAuth):
        self._remote_auth = value

        
    @property
    def children(self) -> List[Child]:
        return self._children

    @children.setter
    def children(self, value: List[Child]):
        self._children = value

        
    @property
    def rekey_time(self) -> None:
        return self._rekey_time

    @rekey_time.setter
    def rekey_time(self, value: None):
        self._rekey_time = value



class ListConnResp:

    def __init__(self, unique, name, ppk, dpd_timeout, reauth_time, ppk_required, version, local_auth, local_addrs, dpd_delay, remote_addrs, remote_auth, children, rekey_time):
        _unique = unique
        _name = name
        _ppk = ppk
        _dpd_timeout = dpd_timeout
        _reauth_time = reauth_time
        _ppk_required = ppk_required
        _version = version
        _local_auth = local_auth
        _local_addrs = local_addrs
        _dpd_delay = dpd_delay
        _remote_addrs = remote_addrs
        _remote_auth = remote_auth
        _children = children
        _rekey_time = rekey_time

        
    @property
    def unique(self) -> str:
        return self._unique

    @unique.setter
    def unique(self, value: str):
        self._unique = value

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

        
    @property
    def ppk(self) -> str:
        return self._ppk

    @ppk.setter
    def ppk(self, value: str):
        self._ppk = value

        
    @property
    def dpd_timeout(self) -> None:
        return self._dpd_timeout

    @dpd_timeout.setter
    def dpd_timeout(self, value: None):
        self._dpd_timeout = value

        
    @property
    def reauth_time(self) -> None:
        return self._reauth_time

    @reauth_time.setter
    def reauth_time(self, value: None):
        self._reauth_time = value

        
    @property
    def ppk_required(self) -> str:
        return self._ppk_required

    @ppk_required.setter
    def ppk_required(self, value: str):
        self._ppk_required = value

        
    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

        
    @property
    def local_auth(self) -> List[ListConnAuth]:
        return self._local_auth

    @local_auth.setter
    def local_auth(self, value: List[ListConnAuth]):
        self._local_auth = value

        
    @property
    def local_addrs(self) -> List[Addrs]:
        return self._local_addrs

    @local_addrs.setter
    def local_addrs(self, value: List[Addrs]):
        self._local_addrs = value

        
    @property
    def dpd_delay(self) -> None:
        return self._dpd_delay

    @dpd_delay.setter
    def dpd_delay(self, value: None):
        self._dpd_delay = value

        
    @property
    def remote_addrs(self) -> List[Addrs]:
        return self._remote_addrs

    @remote_addrs.setter
    def remote_addrs(self, value: List[Addrs]):
        self._remote_addrs = value

        
    @property
    def remote_auth(self) -> List[ListConnAuth]:
        return self._remote_auth

    @remote_auth.setter
    def remote_auth(self, value: List[ListConnAuth]):
        self._remote_auth = value

        
    @property
    def children(self) -> List[ListChild]:
        return self._children

    @children.setter
    def children(self, value: List[ListChild]):
        self._children = value

        
    @property
    def rekey_time(self) -> None:
        return self._rekey_time

    @rekey_time.setter
    def rekey_time(self, value: None):
        self._rekey_time = value



class ListIkeSa:

    def __init__(self, local_host, initiator_spi, remote_vips, ppk, encr_alg, responder_spi, nat_any, nat_fake, rekey_time, if_id_out, established, local_vips, local_port, dh_group, remote_id, integ_keysize, encr_keysize, nat_local, version, tasks_passive, integ_alg, remote_xauth_id, tasks_queued, reauth_time, tasks_active, uniqueid, childsas, initiator, name, nat_remote, remote_port, remote_eap_id, if_id_in, prf_alg, local_id, ikestate, remote_host):
        _local_host = local_host
        _initiator_spi = initiator_spi
        _remote_vips = remote_vips
        _ppk = ppk
        _encr_alg = encr_alg
        _responder_spi = responder_spi
        _nat_any = nat_any
        _nat_fake = nat_fake
        _rekey_time = rekey_time
        _if_id_out = if_id_out
        _established = established
        _local_vips = local_vips
        _local_port = local_port
        _dh_group = dh_group
        _remote_id = remote_id
        _integ_keysize = integ_keysize
        _encr_keysize = encr_keysize
        _nat_local = nat_local
        _version = version
        _tasks_passive = tasks_passive
        _integ_alg = integ_alg
        _remote_xauth_id = remote_xauth_id
        _tasks_queued = tasks_queued
        _reauth_time = reauth_time
        _tasks_active = tasks_active
        _uniqueid = uniqueid
        _childsas = childsas
        _initiator = initiator
        _name = name
        _nat_remote = nat_remote
        _remote_port = remote_port
        _remote_eap_id = remote_eap_id
        _if_id_in = if_id_in
        _prf_alg = prf_alg
        _local_id = local_id
        _ikestate = ikestate
        _remote_host = remote_host

        
    @property
    def local_host(self) -> str:
        return self._local_host

    @local_host.setter
    def local_host(self, value: str):
        self._local_host = value

        
    @property
    def initiator_spi(self) -> str:
        return self._initiator_spi

    @initiator_spi.setter
    def initiator_spi(self, value: str):
        self._initiator_spi = value

        
    @property
    def remote_vips(self) -> List[str]:
        return self._remote_vips

    @remote_vips.setter
    def remote_vips(self, value: List[str]):
        self._remote_vips = value

        
    @property
    def ppk(self) -> str:
        return self._ppk

    @ppk.setter
    def ppk(self, value: str):
        self._ppk = value

        
    @property
    def encr_alg(self) -> str:
        return self._encr_alg

    @encr_alg.setter
    def encr_alg(self, value: str):
        self._encr_alg = value

        
    @property
    def responder_spi(self) -> str:
        return self._responder_spi

    @responder_spi.setter
    def responder_spi(self, value: str):
        self._responder_spi = value

        
    @property
    def nat_any(self) -> str:
        return self._nat_any

    @nat_any.setter
    def nat_any(self, value: str):
        self._nat_any = value

        
    @property
    def nat_fake(self) -> str:
        return self._nat_fake

    @nat_fake.setter
    def nat_fake(self, value: str):
        self._nat_fake = value

        
    @property
    def rekey_time(self) -> str:
        return self._rekey_time

    @rekey_time.setter
    def rekey_time(self, value: str):
        self._rekey_time = value

        
    @property
    def if_id_out(self) -> str:
        return self._if_id_out

    @if_id_out.setter
    def if_id_out(self, value: str):
        self._if_id_out = value

        
    @property
    def established(self) -> str:
        return self._established

    @established.setter
    def established(self, value: str):
        self._established = value

        
    @property
    def local_vips(self) -> List[str]:
        return self._local_vips

    @local_vips.setter
    def local_vips(self, value: List[str]):
        self._local_vips = value

        
    @property
    def local_port(self) -> str:
        return self._local_port

    @local_port.setter
    def local_port(self, value: str):
        self._local_port = value

        
    @property
    def dh_group(self) -> str:
        return self._dh_group

    @dh_group.setter
    def dh_group(self, value: str):
        self._dh_group = value

        
    @property
    def remote_id(self) -> str:
        return self._remote_id

    @remote_id.setter
    def remote_id(self, value: str):
        self._remote_id = value

        
    @property
    def integ_keysize(self) -> str:
        return self._integ_keysize

    @integ_keysize.setter
    def integ_keysize(self, value: str):
        self._integ_keysize = value

        
    @property
    def encr_keysize(self) -> str:
        return self._encr_keysize

    @encr_keysize.setter
    def encr_keysize(self, value: str):
        self._encr_keysize = value

        
    @property
    def nat_local(self) -> str:
        return self._nat_local

    @nat_local.setter
    def nat_local(self, value: str):
        self._nat_local = value

        
    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

        
    @property
    def tasks_passive(self) -> List[str]:
        return self._tasks_passive

    @tasks_passive.setter
    def tasks_passive(self, value: List[str]):
        self._tasks_passive = value

        
    @property
    def integ_alg(self) -> str:
        return self._integ_alg

    @integ_alg.setter
    def integ_alg(self, value: str):
        self._integ_alg = value

        
    @property
    def remote_xauth_id(self) -> str:
        return self._remote_xauth_id

    @remote_xauth_id.setter
    def remote_xauth_id(self, value: str):
        self._remote_xauth_id = value

        
    @property
    def tasks_queued(self) -> List[str]:
        return self._tasks_queued

    @tasks_queued.setter
    def tasks_queued(self, value: List[str]):
        self._tasks_queued = value

        
    @property
    def reauth_time(self) -> str:
        return self._reauth_time

    @reauth_time.setter
    def reauth_time(self, value: str):
        self._reauth_time = value

        
    @property
    def tasks_active(self) -> List[str]:
        return self._tasks_active

    @tasks_active.setter
    def tasks_active(self, value: List[str]):
        self._tasks_active = value

        
    @property
    def uniqueid(self) -> str:
        return self._uniqueid

    @uniqueid.setter
    def uniqueid(self, value: str):
        self._uniqueid = value

        
    @property
    def childsas(self) -> List[ListChildSa]:
        return self._childsas

    @childsas.setter
    def childsas(self, value: List[ListChildSa]):
        self._childsas = value

        
    @property
    def initiator(self) -> str:
        return self._initiator

    @initiator.setter
    def initiator(self, value: str):
        self._initiator = value

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

        
    @property
    def nat_remote(self) -> str:
        return self._nat_remote

    @nat_remote.setter
    def nat_remote(self, value: str):
        self._nat_remote = value

        
    @property
    def remote_port(self) -> str:
        return self._remote_port

    @remote_port.setter
    def remote_port(self, value: str):
        self._remote_port = value

        
    @property
    def remote_eap_id(self) -> str:
        return self._remote_eap_id

    @remote_eap_id.setter
    def remote_eap_id(self, value: str):
        self._remote_eap_id = value

        
    @property
    def if_id_in(self) -> str:
        return self._if_id_in

    @if_id_in.setter
    def if_id_in(self, value: str):
        self._if_id_in = value

        
    @property
    def prf_alg(self) -> str:
        return self._prf_alg

    @prf_alg.setter
    def prf_alg(self, value: str):
        self._prf_alg = value

        
    @property
    def local_id(self) -> str:
        return self._local_id

    @local_id.setter
    def local_id(self, value: str):
        self._local_id = value

        
    @property
    def ikestate(self) -> None:
        return self._ikestate

    @ikestate.setter
    def ikestate(self, value: None):
        self._ikestate = value

        
    @property
    def remote_host(self) -> str:
        return self._remote_host

    @remote_host.setter
    def remote_host(self, value: str):
        self._remote_host = value



class ListCert:
    """ list-cert """
    def __init__(self, notbefore, type, notafter, flag, hasprivkey, data, subject):
        _notbefore = notbefore
        _type = type
        _notafter = notafter
        _flag = flag
        _hasprivkey = hasprivkey
        _data = data
        _subject = subject

        
    @property
    def notbefore(self) -> str:
        return self._notbefore

    @notbefore.setter
    def notbefore(self, value: str):
        self._notbefore = value

        
    @property
    def type(self) -> None:
        return self._type

    @type.setter
    def type(self, value: None):
        self._type = value

        
    @property
    def notafter(self) -> str:
        return self._notafter

    @notafter.setter
    def notafter(self, value: str):
        self._notafter = value

        
    @property
    def flag(self) -> None:
        return self._flag

    @flag.setter
    def flag(self, value: None):
        self._flag = value

        
    @property
    def hasprivkey(self) -> str:
        return self._hasprivkey

    @hasprivkey.setter
    def hasprivkey(self, value: str):
        self._hasprivkey = value

        
    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str):
        self._data = value

        
    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, value: str):
        self._subject = value



class IPsecLoadConnRequest:

    def __init__(self, connection):
        _connection = connection

        
    @property
    def connection(self) -> Connection:
        return self._connection

    @connection.setter
    def connection(self, value: Connection):
        self._connection = value



class IPsecVersionResponse:

    def __init__(self, release, sysname, daemon, version, machine):
        _release = release
        _sysname = sysname
        _daemon = daemon
        _version = version
        _machine = machine

        
    @property
    def release(self) -> str:
        return self._release

    @release.setter
    def release(self, value: str):
        self._release = value

        
    @property
    def sysname(self) -> str:
        return self._sysname

    @sysname.setter
    def sysname(self, value: str):
        self._sysname = value

        
    @property
    def daemon(self) -> str:
        return self._daemon

    @daemon.setter
    def daemon(self, value: str):
        self._daemon = value

        
    @property
    def version(self) -> str:
        return self._version

    @version.setter
    def version(self, value: str):
        self._version = value

        
    @property
    def machine(self) -> str:
        return self._machine

    @machine.setter
    def machine(self, value: str):
        self._machine = value



class IPsecInitiateRequest:

    def __init__(self, loglevel, timeout, ike, child):
        _loglevel = loglevel
        _timeout = timeout
        _ike = ike
        _child = child

        
    @property
    def loglevel(self) -> str:
        return self._loglevel

    @loglevel.setter
    def loglevel(self, value: str):
        self._loglevel = value

        
    @property
    def timeout(self) -> str:
        return self._timeout

    @timeout.setter
    def timeout(self, value: str):
        self._timeout = value

        
    @property
    def ike(self) -> str:
        return self._ike

    @ike.setter
    def ike(self, value: str):
        self._ike = value

        
    @property
    def child(self) -> str:
        return self._child

    @child.setter
    def child(self, value: str):
        self._child = value



class IPsecRekeyRequest:

    def __init__(self, ike_id, child_id, reauth, ike, child):
        _ike_id = ike_id
        _child_id = child_id
        _reauth = reauth
        _ike = ike
        _child = child

        
    @property
    def ike_id(self) -> str:
        return self._ike_id

    @ike_id.setter
    def ike_id(self, value: str):
        self._ike_id = value

        
    @property
    def child_id(self) -> str:
        return self._child_id

    @child_id.setter
    def child_id(self, value: str):
        self._child_id = value

        
    @property
    def reauth(self) -> str:
        return self._reauth

    @reauth.setter
    def reauth(self, value: str):
        self._reauth = value

        
    @property
    def ike(self) -> str:
        return self._ike

    @ike.setter
    def ike(self, value: str):
        self._ike = value

        
    @property
    def child(self) -> str:
        return self._child

    @child.setter
    def child(self, value: str):
        self._child = value



class IPsecListConnsResponse:

    def __init__(self, connection):
        _connection = connection

        
    @property
    def connection(self) -> List[ListConnResp]:
        return self._connection

    @connection.setter
    def connection(self, value: List[ListConnResp]):
        self._connection = value



class IPsecTerminateRequest:

    def __init__(self, force, ike, loglevel, timeout, child, ike_id, child_id):
        _force = force
        _ike = ike
        _loglevel = loglevel
        _timeout = timeout
        _child = child
        _ike_id = ike_id
        _child_id = child_id

        
    @property
    def force(self) -> str:
        return self._force

    @force.setter
    def force(self, value: str):
        self._force = value

        
    @property
    def ike(self) -> str:
        return self._ike

    @ike.setter
    def ike(self, value: str):
        self._ike = value

        
    @property
    def loglevel(self) -> str:
        return self._loglevel

    @loglevel.setter
    def loglevel(self, value: str):
        self._loglevel = value

        
    @property
    def timeout(self) -> str:
        return self._timeout

    @timeout.setter
    def timeout(self, value: str):
        self._timeout = value

        
    @property
    def child(self) -> str:
        return self._child

    @child.setter
    def child(self, value: str):
        self._child = value

        
    @property
    def ike_id(self) -> str:
        return self._ike_id

    @ike_id.setter
    def ike_id(self, value: str):
        self._ike_id = value

        
    @property
    def child_id(self) -> str:
        return self._child_id

    @child_id.setter
    def child_id(self, value: str):
        self._child_id = value



class IPsecInitiateResponse:
    """ Intentionally empty """
    def __init__(self, ):
        pass


class IPsecStatsRequest:
    """ Intentionally empty """
    def __init__(self, ):
        pass


class IPsecVersionRequest:
    """ Intentionally empty """
    def __init__(self, ):
        pass


class IPsecLoadConnResponse:

    def __init__(self, success):
        _success = success

        
    @property
    def success(self) -> str:
        return self._success

    @success.setter
    def success(self, value: str):
        self._success = value



class IPsecStatsResponse:

    def __init__(self, status):
        _status = status

        
    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value



class IPsecUnloadConnRequest:

    def __init__(self, name):
        _name = name

        
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value



class IPsecTerminateResponse:

    def __init__(self, matches, terminated, success):
        _matches = matches
        _terminated = terminated
        _success = success

        
    @property
    def matches(self) -> None:
        return self._matches

    @matches.setter
    def matches(self, value: None):
        self._matches = value

        
    @property
    def terminated(self) -> None:
        return self._terminated

    @terminated.setter
    def terminated(self, value: None):
        self._terminated = value

        
    @property
    def success(self) -> str:
        return self._success

    @success.setter
    def success(self, value: str):
        self._success = value



class IPsecListSasRequest:

    def __init__(self, ike_id, child_id, child, ike, noblock):
        _ike_id = ike_id
        _child_id = child_id
        _child = child
        _ike = ike
        _noblock = noblock

        
    @property
    def ike_id(self) -> str:
        return self._ike_id

    @ike_id.setter
    def ike_id(self, value: str):
        self._ike_id = value

        
    @property
    def child_id(self) -> str:
        return self._child_id

    @child_id.setter
    def child_id(self, value: str):
        self._child_id = value

        
    @property
    def child(self) -> str:
        return self._child

    @child.setter
    def child(self, value: str):
        self._child = value

        
    @property
    def ike(self) -> str:
        return self._ike

    @ike.setter
    def ike(self, value: str):
        self._ike = value

        
    @property
    def noblock(self) -> str:
        return self._noblock

    @noblock.setter
    def noblock(self, value: str):
        self._noblock = value



class IPsecListSasResponse:

    def __init__(self, ikesas):
        _ikesas = ikesas

        
    @property
    def ikesas(self) -> List[ListIkeSa]:
        return self._ikesas

    @ikesas.setter
    def ikesas(self, value: List[ListIkeSa]):
        self._ikesas = value



class IPsecListConnsRequest:

    def __init__(self, ike):
        _ike = ike

        
    @property
    def ike(self) -> str:
        return self._ike

    @ike.setter
    def ike(self, value: str):
        self._ike = value



class IPsecListCertsRequest:

    def __init__(self, flag, type, subject):
        _flag = flag
        _type = type
        _subject = subject

        
    @property
    def flag(self) -> str:
        return self._flag

    @flag.setter
    def flag(self, value: str):
        self._flag = value

        
    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value

        
    @property
    def subject(self) -> str:
        return self._subject

    @subject.setter
    def subject(self, value: str):
        self._subject = value



class IPsecRekeyResponse:

    def __init__(self, matches, success):
        _matches = matches
        _success = success

        
    @property
    def matches(self) -> None:
        return self._matches

    @matches.setter
    def matches(self, value: None):
        self._matches = value

        
    @property
    def success(self) -> str:
        return self._success

    @success.setter
    def success(self, value: str):
        self._success = value



class IPsecListCertsResponse:

    def __init__(self, certs):
        _certs = certs

        
    @property
    def certs(self) -> List[ListCert]:
        return self._certs

    @certs.setter
    def certs(self, value: List[ListCert]):
        self._certs = value



class IPsecUnloadConnResponse:

    def __init__(self, success):
        _success = success

        
    @property
    def success(self) -> str:
        return self._success

    @success.setter
    def success(self, value: str):
        self._success = value


