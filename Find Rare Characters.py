import operator
def listo(data):
    chars = {}
    for ch in data:
        chars[ch] = chars.get(ch, 0) + 1
    return sorted(sorted(sorted(chars.items()), key=operator.itemgetter(1))[:5])

data="""(+*]_}%+(%[{)]({#[+$&&[^@{&#!@%)!+&}$@+@[+&_*!$(+#*%!+$@{{^**{)(]*$(}+(#+^}%@%^^
!$%}$$}+@^$$%{}{#!(%[]$!*}+(]!%{(^{&^{$[$)]&&^+{+%!#[([%^!{]]#^@!{#(&]@_$*_&!%(!
+_+}%@#{_}^#*)%*(*}*![}[%_[[^@$&%)([*{_${)$^^_!+}{)!)@_[*$_}*}$#[+}{]*+!^])}&{+#
+!@!^*@}!}&{]*#^@}_[)}#@%!_*#!$}!)[(${+^&!{[&&&*[{}+*+(#+_[}{$$)#([*!)%@^%_]#%$$
(++^+&)}*_&%@#[^^+^&@_%]+$%$#$*)@!(]*+@]}%$$}$(#$&^(%[*([&]*^&}(!#{&_}^(*{(+$#}}"""
print(listo(data))