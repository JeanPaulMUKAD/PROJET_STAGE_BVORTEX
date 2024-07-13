/**@odoo-module **/
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {Component} from "@odoo/owl";

const actionRegistry = registry.category("actions");

class ControlDocumentDashboard extends Component {

    setup() {
        super.setup();
        this.orm = useService('orm');
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

}

ControlDocumentDashboard.template = "bvortex_controls.ControlDocumentDashboard";
actionRegistry.add("dashboard_control_document_tag", ControlDocumentDashboard);