import pandas as pd
from pathlib import Path


class WSection:
    cwd = Path(__file__).parent
    E = 206000
    __doc__ = """This progarm can get properties of w-section steel beam
    Axis Definition:
                 ↑y
                 |
           ============
                 ‖
                 ‖        x
         --------‖--------→
                 ‖
                 ‖
           ============
                 |
    d: Depth
    bf: Top width
    tf: Flange thickness
    tw: Web thickness
    r: Fillet radius
    A: Area
    J: Torsion constant
    Iy: Moment of inertia about y-axis
    Ix: Moment of inertia about x-axis
    Alpha: Principal axis angle
    Iw: Warping constant
    Zy: Plastic modulars about y-axis
    Zx: Plastic modulars about x-axis
    (All units are in "mm" or "N")

    Update: 2024-03-14
    """


    def __init__(self, section: str, fy: float=None):
        """get section property with given section name 

        Args:
            section (str): section name
            fy (float, optional): yield strength (Dafault to None).

        Example:
            >>> section = WSection('W14x90', fy=345)
        """
        self.section = section
        try:
            section_data = pd.read_csv(self.cwd / 'W-section.csv')
        except:
            raise FileNotFoundError('"W-section.csv" not found!')
        try:
            data = section_data.loc[section_data['section'] == self.section].iloc[0].tolist()
        except:
            raise ValueError(f'"{self.section}" not found!')
        self.name, self.d, self.bf, self.tf, self._bf_bottom, self._tf_bottom, self.tw, self.r, self.A,\
            self.J, self.Iy, self.Ix, self.Alpha, self.Cy, self.Cx, self.Iw, self.Zy, self.Zx = data
        self.h = self.d - 2 * self.tf - 2 * self.r
        self.ry = (self.Iy / self.A) ** 0.5
        self.rx = (self.Ix / self.A) ** 0.5
        self.Wy = self.Iy / (self.d / 2)
        self.Wx = self.Ix / (self.d / 2)
        if fy:
            self.fy = fy
            # self.My = self.fy * self.Wx * 1.1
            self.My = self.fy * self.Zx
        

    def __getattr__(self, name):
        if name == 'My' or name == 'fy':
            raise AttributeError('Please define parameter `fy` first.')

    def set_fy(self, fy: int):
        """set yield strength of steel to calculate My.

        Args:
            fy (int): yield strength
        """
        self.fy = fy
        # self.My = self.fy * self.Wx * 1.1
        self.My = self.fy * self.Zx

    @classmethod
    def list_sections(cls) -> list:
        """list all sections

        Returns:
            list: a list includes all section names
        """
        try:
            section_data = pd.read_csv(cls.cwd / 'W-section.csv')
        except:
            raise FileNotFoundError('"W-section.csv" not found!')
        
        return section_data['section'].to_list()



    


