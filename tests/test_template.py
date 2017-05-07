from cjrh_template import cjrhTemplate as Template


def test_basic():
    s = '$person1 gave $thing to $person2'
    tmpl = Template(s)
    assert set(tmpl.template_vars()) == {'person1', 'thing', 'person2'}


def test_repeat_set():
    s = '$person1 gave $thing to $person2. $person1 was happy'
    tmpl = Template(s)
    assert set(tmpl.template_vars()) == {'person1', 'thing', 'person2'}


def test_repeat_list():
    s = '$person1 gave $thing to $person2. $person1 was happy'
    tmpl = Template(s)
    assert list(tmpl.template_vars()) == ['person1', 'thing', 'person2']


def test_repeat_list_repeat():
    s = '$person1 gave $thing to $person2. $person1 was happy'
    names = ['person1', 'thing', 'person2', 'person1']
    tmpl = Template(s)
    assert list(tmpl.template_vars(allow_repeats=True)) == names
