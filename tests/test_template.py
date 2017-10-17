from cjrh_template import Template


def test_basic():
    s = '$person1 gave $thing to $person2'
    tmpl = Template(s)
    assert set(tmpl.placeholders()) == {'person1', 'thing', 'person2'}


def test_repeat_set():
    s = '$person1 gave $thing to $person2. $person1 was happy'
    tmpl = Template(s)
    assert set(tmpl.placeholders()) == {'person1', 'thing', 'person2'}


def test_repeat_list():
    s = '$person1 gave $thing to $person2. $person1 was happy'
    tmpl = Template(s)
    assert list(tmpl.placeholders()) == ['person1', 'thing', 'person2']


def test_repeat_list_repeat():
    s = '$person1 gave $thing to $person2. $person1 was happy'
    names = ['person1', 'thing', 'person2', 'person1']
    tmpl = Template(s)
    assert list(tmpl.placeholders(allow_repeats=True)) == names


def test_empty():
    s = 'This has\nno\nplaceholders\nwhatsoever'
    tmpl = Template(s)
    assert list(tmpl.placeholders()) == []


def test_makefile():
    s = '$(shell find $(SRC_DIRS))'
    tmpl = Template(s)
    assert list(tmpl.placeholders()) == []
