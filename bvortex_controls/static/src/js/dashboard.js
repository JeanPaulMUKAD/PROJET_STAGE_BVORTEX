/**@odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component} from "@odoo/owl";

const actionRegistry = registry.category("actions");

class ControlDocumentDashboard extends Component {

    setup() {
        super.setup();
        this.orm = useService('orm');
        this.action = useService('action');
        this._fetch_data();
    }

    _fetch_data() {
        const self = this;
        this.orm.call("control.document.dashboard", "get_all_data", [], {}).then(function (result) {
            $('#atd').append('<span>' + result.atd + '<span/>');
            $('#avis_de_verification').append('<span>' + result.avis_de_verification + '<span/>');
            $('#contrainte').append('<span>' + result.contrainte + '<span/>');
            $('#notification_penal').append('<span>' + result.notification_penal + '<span/>');
            $('#amrs').append('<span>' + result.amrs + '<span/>');
            $('#med').append('<span>' + result.med + '<span/>');
            $('#avis_taxation').append('<span>' + result.avis_taxation + '<span/>');
            $('#invitation_serv').append('<span>' + result.invitation_serv + '<span/>');
            $('#avis_regulation').append('<span>' + result.avis_regulation + '<span/>');
            $('#demande_renseign').append('<span>' + result.demande_renseign + '<span/>');
            $('#dgrad').append('<span>' + result.dgrad + '<span/>');
            $('#economie').append('<span>' + result.economie + '<span/>');
            $('#environement').append('<span>' + result.environement + '<span/>');
            $('#inspection_travail').append('<span>' + result.inspection_travail + '<span/>');
            $('#cotisation_soc_autres').append('<span>' + result.cotisation_soc_autres + '<span/>');
            $('#declarations').append('<span>' + result.declarations + '<span/>');
            $('#descente_terrain').append('<span>' + result.descente_terrain + '<span/>');
            $('#rdv_prospection').append('<span>' + result.rdv_prospection + '<span/>');
            $('#avis_technique').append('<span>' + result.avis_technique + '<span/>');
            $('#tache_en_cours').append('<span>' + result.tache_en_cours + '<span/>');
        });
    };

    onLinkClick(ev) {
        ev.preventDefault();
        const id = ev.currentTarget.id;
        this.orm.call("control.document.dashboard", "on_link_click", [id], {}).then((result) => {
            this.action.doAction(result);
        });
    }


}
ControlDocumentDashboard.template = "bvortex_controls.ControlDocumentDashboard";
actionRegistry.add("dashboard_control_document_tag", ControlDocumentDashboard);



class ControlDeclarationDashboard2 extends Component {

 setup() {
        super.setup();
        this.orm = useService('orm');
        this.action = useService('action');
        this._fetch_data();
    }

    _fetch_data() {
        const self = this;
        this.orm.call("control.document.dashboard", "get_all_data", [], {}).then(function (result) {

            $('#etablie_nbr').append('<span>' + result.etablie_nbr + '<span/>');
            $('#revue_nbr').append('<span>' + result.revue_nbr + '<span/>');
            $('#valider_nbr').append('<span>' + result.valider_nbr + '<span/>');
            $('#payer_nbr').append('<span>' + result.payer_nbr + '<span/>');
            $('#declarer_nbr').append('<span>' + result.declarer_nbr + '<span/>');
            $('#apurer_nbr').append('<span>' + result.apurer_nbr + '<span/>');
            $('#archiver_nbr').append('<span>' + result.archiver_nbr + '<span/>');
            $('#transmit_nbr').append('<span>' + result.transmit_nbr + '<span/>');

             $('#etablie2_nbr').append('<span>' + result.etablie2_nbr + '<span/>');
            $('#revue2_nbr').append('<span>' + result.revue2_nbr + '<span/>');
            $('#valider2_nbr').append('<span>' + result.valider2_nbr + '<span/>');
            $('#payer2_nbr').append('<span>' + result.payer2_nbr + '<span/>');
            $('#declarer2_nbr').append('<span>' + result.declarer2_nbr + '<span/>');
            $('#apurer2_nbr').append('<span>' + result.apurer2_nbr + '<span/>');
            $('#archiver2_nbr').append('<span>' + result.archiver2_nbr + '<span/>');
            $('#transmit2_nbr').append('<span>' + result.transmit2_nbr + '<span/>');

             $('#etablie3_nbr').append('<span>' + result.etablie3_nbr + '<span/>');
            $('#revue3_nbr').append('<span>' + result.revue3_nbr + '<span/>');
            $('#valider3_nbr').append('<span>' + result.valider3_nbr + '<span/>');
            $('#payer3_nbr').append('<span>' + result.payer3_nbr + '<span/>');
            $('#declarer3_nbr').append('<span>' + result.declarer3_nbr + '<span/>');
            $('#apurer3_nbr').append('<span>' + result.apurer3_nbr + '<span/>');
            $('#archiver3_nbr').append('<span>' + result.archiver3_nbr + '<span/>');
            $('#transmit3_nbr').append('<span>' + result.transmit3_nbr + '<span/>');

             $('#etablie4_nbr').append('<span>' + result.etablie4_nbr + '<span/>');
            $('#revue4_nbr').append('<span>' + result.revue4_nbr + '<span/>');
            $('#valider4_nbr').append('<span>' + result.valider4_nbr + '<span/>');
            $('#payer4_nbr').append('<span>' + result.payer4_nbr + '<span/>');
            $('#declarer4_nbr').append('<span>' + result.declarer4_nbr + '<span/>');
            $('#apurer4_nbr').append('<span>' + result.apurer4_nbr + '<span/>');
            $('#archiver4_nbr').append('<span>' + result.archiver4_nbr + '<span/>');
            $('#transmit4_nbr').append('<span>' + result.transmit4_nbr + '<span/>');

            $('#etablie5_nbr').append('<span>' + result.etablie5_nbr + '<span/>');
            $('#revue5_nbr').append('<span>' + result.revue5_nbr + '<span/>');
            $('#valider5_nbr').append('<span>' + result.valider5_nbr + '<span/>');
            $('#payer5_nbr').append('<span>' + result.payer5_nbr + '<span/>');
            $('#declarer5_nbr').append('<span>' + result.declarer5_nbr + '<span/>');
            $('#apurer5_nbr').append('<span>' + result.apurer5_nbr + '<span/>');
            $('#archiver5_nbr').append('<span>' + result.archiver5_nbr + '<span/>');
            $('#transmit5_nbr').append('<span>' + result.transmit5_nbr + '<span/>');

            $('#etablie6_nbr').append('<span>' + result.etablie6_nbr + '<span/>');
            $('#revue6_nbr').append('<span>' + result.revue6_nbr + '<span/>');
            $('#valider6_nbr').append('<span>' + result.valider6_nbr + '<span/>');
            $('#payer6_nbr').append('<span>' + result.payer6_nbr + '<span/>');
            $('#declarer6_nbr').append('<span>' + result.declarer6_nbr + '<span/>');
            $('#apurer6_nbr').append('<span>' + result.apurer6_nbr + '<span/>');
            $('#archiver6_nbr').append('<span>' + result.archiver6_nbr + '<span/>');
            $('#transmit6_nbr').append('<span>' + result.transmit6_nbr + '<span/>');

            $('#etablie7_nbr').append('<span>' + result.etablie7_nbr + '<span/>');
            $('#revue7_nbr').append('<span>' + result.revue7_nbr + '<span/>');
            $('#valider7_nbr').append('<span>' + result.valider7_nbr + '<span/>');
            $('#payer7_nbr').append('<span>' + result.payer7_nbr + '<span/>');
            $('#declarer7_nbr').append('<span>' + result.declarer7_nbr + '<span/>');
            $('#apurer7_nbr').append('<span>' + result.apurer7_nbr + '<span/>');
            $('#archiver7_nbr').append('<span>' + result.archiver7_nbr + '<span/>');
            $('#transmit7_nbr').append('<span>' + result.transmit7_nbr + '<span/>');

        });
    };

 onLinkClick(ev) {
        ev.preventDefault();
        const id = ev.currentTarget.id;
        this.orm.call("control.document.dashboard", "on_link_click", [id], {}).then((result) => {
            this.action.doAction(result);
        });
    }

}
ControlDeclarationDashboard2.template = "bvortex_controls.ControlDeclarationDashboard2";
actionRegistry.add("dashboard_declaration_document_tag", ControlDeclarationDashboard2);



class ControlStatitiqueDashboard3 extends Component {
    setup() {
        super.setup();
        this.orm = useService('orm');
        this.action = useService('action');

        const selectElement = document.getElementById('element-selection');
        if (selectElement) {
            selectElement.addEventListener('change', this.onSelectChange.bind(this));
        }
         const currentYear = new Date().getFullYear();
        this.years = Array.from({ length: 25 }, (_, i) => currentYear - i); // Génère les 25 dernières années

        this.selectedYear = currentYear;
    }

     onYearChange(ev) {
        const selectedYear = ev.target.value;
        console.log("Année sélectionnée :", selectedYear);
        this.selectedYear = selectedYear;
    }

   onSelectChange(ev) {
        const selectedValue = ev.target.value;
        console.log("Valeur sélectionnée :", selectedValue);
        this.selectedValue = selectedValue;
    }

    onLinkClick(ev) {
        ev.preventDefault();
        const id = ev.currentTarget.id;

        const selectElement = document.getElementById('element-selection');
        const selectedValue = selectElement ? selectElement.value : null;

        const yearElement = document.getElementById('year-selection');
        const selectedYear = yearElement ? yearElement.value : null;

        console.log("Lien cliqué avec id:", id, "et selectedValue:", selectedValue);
        console.log("Lien cliqué avec id:", id, "et année sélectionnée:", selectedYear);

        this.orm.call("control.document.dashboard", "on_link_click", [id, selectedValue, selectedYear], {})
            .then((result) => {
                console.log('Result from server:', result);
                this.action.doAction(result);
            })
            .catch((error) => {
                console.error('RPC Error:', error);
            });
    }
}

ControlStatitiqueDashboard3.template = "bvortex_controls.ControlStatitiqueDashboard3";
actionRegistry.add("dashboard_statistique_document_tag", ControlStatitiqueDashboard3);