from persistent import Persistent
from zope.interface import Attribute
from zope.interface import implements
from zope.interface.interface import Interface
from zope.component import getUtility


class ITaggingConfig(Interface):
    use_exif = Attribute("Boolean describing if exif should be converted to tags")

    use_iptc = Attribute("Boolean describing if iptc should be converted to tags")

    use_title = Attribute("Boolean describing if title should be converted to tags")

    exif_fields = Attribute("List holding information for converting exif")

    iptc_fields = Attribute("List holding information for converting iptc")

    ignored_tags = Attribute("List holding information for ignoring tags")


class TaggingConfig(Persistent):
    implements(ITaggingConfig)

    _use_exif = True
    _use_iptc = True
    _use_title = True
    _exif_fields = []
    _iptc_fields = []
    _ignored_tags = []
    _test_image = None

    @property
    def use_exif(self):
        return self._use_exif

    @use_exif.setter
    def use_exif(self, value):
        self._use_exif = value
        self._p_changed = True

    @property
    def use_iptc(self):
        return self._use_iptc

    @use_iptc.setter
    def use_iptc(self, value):
        self._use_iptc = value
        self._p_changed = True

    @property
    def use_title(self):
        return self._use_title

    @use_title.setter
    def use_title(self, value):
        self._use_title = value
        self._p_changed = True

    @property
    def exif_fields(self):
        return self._exif_fields

    @exif_fields.setter
    def exif_fields(self, value):
        self._exif_fields = value
        self._p_changed = True

    @property
    def iptc_fields(self):
        return self._iptc_fields

    @iptc_fields.setter
    def iptc_fields(self, value):
        self._iptc_fields = value
        self._p_changed = True

    @property
    def ignored_tags(self):
        return self._ignored_tags

    @ignored_tags.setter
    def ignored_tags(self, value):
        self._ignored_tags = value
        self._p_changed = True

    @property
    def test_image(self):
        return self._test_image

    @test_image.setter
    def test_image(self, value):
        self._test_image = value
        self._p_changed = True

    def add_exif_tag(self, tag):
        self.exif_fields.append({
            'regex': '',
            'field': tag,
            'format': ''
        })

    def add_iptc_tag(self, tag):
        self.iptc_fields.append({
            'regex': '',
            'field': tag,
            'format': ''
        })


def get_use_exif():
    config_store = getUtility(ITaggingConfig)
    return config_store.use_exif


def get_use_iptc():
    config_store = getUtility(ITaggingConfig)
    return config_store.use_iptc


def get_use_title():
    config_store = getUtility(ITaggingConfig)
    return config_store.use_title


def get_exif_fields():
    config_store = getUtility(ITaggingConfig)
    return config_store.exif_fields


def get_iptc_fields():
    config_store = getUtility(ITaggingConfig)
    return config_store.iptc_fields


def get_ignored_tags():
    config_store = getUtility(ITaggingConfig)
    return config_store.ignored_tags

def get_test_image():
    config_store = getUtility(ITaggingConfig)
    return config_store.test_image