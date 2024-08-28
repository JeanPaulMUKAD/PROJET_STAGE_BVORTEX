/** @odoo-module **/
import { SwitchCompanyMenu } from "@web/webclient/switch_company_menu/switch_company_menu";
import { patch } from "@web/core/utils/patch";

patch(SwitchCompanyMenu.prototype, {
    setup() {
        super.setup(); // Appel du setup de la classe parente
        this.allCompanyIds = Object.values(this.companyService.allowedCompanies).map(x => x.id);

        this.isAllCompaniesSelected = this.allCompanyIds.every((id) =>
            this.companySelector.selectedCompaniesIds.includes(id)
        );
    },

    async toggleSelectAllCompanies() {
        try {
            if (this.isAllCompaniesSelected) {
                // Désélectionner toutes les sociétés
                this.isAllCompaniesSelected = false;
                for (let id of this.allCompanyIds) {
                    if (this.companySelector.selectedCompaniesIds.includes(id)) {
                        console.log(id);
                        await this.companySelector.switchCompany("toggle", id); // Utilisation d'une attente asynchrone
                    }
                }
            } else {
                // Sélectionner toutes les sociétés
                this.isAllCompaniesSelected = true;
                for (let id of this.allCompanyIds) {
                    if (!this.companySelector.selectedCompaniesIds.includes(id)) {
                        console.log(id);
                        await this.companySelector.switchCompany("toggle", id); // Utilisation d'une attente asynchrone
                    }
                }
            }
        } catch (error) {
            console.error("An error occurred while toggling companies:", error);
        }
    },
});
