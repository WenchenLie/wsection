## Steel section helper
A tool for obtaining information about steel sections. Available sections include w-seciton (AISC), and H-section from Chinese code.
## Example
Install the package using pip or conda:
```console
pip install wsection
```
Institute a section object:
```python
# create a w-section (AISC)
from wsection import WSection
section = WSection('W14x90')

# create a GB-section (Chinese code)
from wsection import GBSection
HMsection = GBSection('HM148x100')
HNsection = GBSection('HN250x125')
HWsection = GBSection('HW250x125')
```
Get section properties
```python
print(section.d)  # depth
print(section.bf)  # flange width
print(section.tw)  # web thickness
print(section.tf)  # flange thickness
print(section.A)  # Area
print(section.Ix)  # Moment of inertia
print(section.Zx)  # Plastic modulars
```