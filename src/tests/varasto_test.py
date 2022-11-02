import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.toinen_varasto = Varasto(-10)
        self.kolmas_varasto = Varasto(20, 40)
        self.neljas_varasto = Varasto(10, -10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_tilavuus_ei_voi_olla_negatiivinen(self):
        self.assertAlmostEqual(self.toinen_varasto.tilavuus, 0)

    def test_alkusaldo_ei_voi_olla_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.kolmas_varasto.saldo, 20)

    def test_alkusaldo_ei_voi_olla_negatiivinen(self):
        self.assertAlmostEqual(self.neljas_varasto.saldo, 0)


    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_voi_lisata_enempaa_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(12)
        self.assertAlmostEqual(self.varasto.saldo, 10)


    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(9)
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 9)

    def test_ei_voi_ottaa_enempaa_kuin_varastossa_on(self):
        self.varasto.lisaa_varastoon(5)
        otettu_maara = self.varasto.ota_varastosta(6)
        self.assertAlmostEqual(otettu_maara, 5)

    def test_tulostus_oikein(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")
