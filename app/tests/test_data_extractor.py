from data_extractor import DataExtractor
import urllib.request
import pytest


class TestAPI:
    def test_exception(self, monkeypatch):
        name = "Lognes"
        if name == "Lognes":
            def mockreturn():
                return name
        else:
            raise Exception("Nom invalide")

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    def test_place_name_exception(self):
        """test that exception is raised for invalid place name"""
        with pytest.raises(Exception):
            assert self.test_exception() != "Mogn"

    def test_get_gm_http_return(self, monkeypatch):
        results = [{
            "address": "77185 Lognes, France",
            "lat": 48.836571,
            "lng": 2.6327379
            }]

        def mockreturn():
            return results

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        gm_test = DataExtractor()
        assert gm_test.get_gm_data("Lognes") == results

    def test_get_wm_http_return(self, monkeypatch):
        extract = {"extract": "Paris (/pa.ʁi/) est la commune la plus peuplée et la capitale de la France.\nElle se situe "
                              "au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, "
                              "le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la "
                              "Marne et l'Oise. Paris est également le chef-lieu de la région Île-de-France et le centre "
                              "de la métropole du Grand Paris, créée en 2016. Elle est divisée en arrondissements, "
                              "comme les villes de Lyon et de Marseille, au nombre de vingt. Administrativement, "
                              "la ville constitue depuis le 1er janvier 2019 une collectivité à statut particulier nommée "
                              "« Ville de Paris » (auparavant, elle était à la fois une commune et un département)."}

        def mockreturn():
            return extract

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
        wm_test = DataExtractor()
        assert wm_test.get_mw_data("Paris") == extract

    def test_get_key_words(self):
        key_words = DataExtractor()
        key_words.get_key_words("Où se trouve Paris ?")
        results = "paris"
        assert key_words.get_key_words("Où se trouve Paris ?") == results

    def test_get_gm_data(self):
        place_data = DataExtractor()
        place_data.get_gm_data("Paris")
        data = {"address": "Paris, France", "lat": 48.856614, "lng": 2.3522219}
        assert place_data.get_gm_data("Paris") == [{"address": data["address"], "lat":data["lat"], "lng": data["lng"]}]

    def test_get_mw_data(self):
        name_place = DataExtractor()
        name_place.get_mw_data("Paris")
        extract = {"extract": "Paris (/pa.ʁi/) est la commune la plus peuplée et la capitale de la France.\nElle se situe "
                              "au cœur d'un vaste bassin sédimentaire aux sols fertiles et au climat tempéré, "
                              "le bassin parisien, sur une boucle de la Seine, entre les confluents de celle-ci avec la "
                              "Marne et l'Oise. Paris est également le chef-lieu de la région Île-de-France et le centre "
                              "de la métropole du Grand Paris, créée en 2016. Elle est divisée en arrondissements, "
                              "comme les villes de Lyon et de Marseille, au nombre de vingt. Administrativement, "
                              "la ville constitue depuis le 1er janvier 2019 une collectivité à statut particulier nommée "
                              "« Ville de Paris » (auparavant, elle était à la fois une commune et un département)."}

        assert name_place.get_mw_data("Paris") == extract
