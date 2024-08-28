/** @odoo-module **/
import {SwitchCompanyMenu} from "@web/webclient/switch_company_menu/switch_company_menu";
import {patch} from "@web/core/utils/patch";

patch(SwitchCompanyMenu.prototype, {
    setup() {
        super.setup();
        this.allCompanyIds = Object.values(this.companyService.allowedCompanies).map(x => x.id);

        this.isAllCompaniesSelected = this.allCompanyIds.every((id) =>
            this.companySelector.selectedCompaniesIds.includes(id)
        );
    },

    toggleSelectAllCompanies() {
        if (this.isAllCompaniesSelected) {
            // Deselect all companies
            this.isAllCompaniesSelected = false;
            this.allCompanyIds.forEach((id) => {
                if (this.companySelector.selectedCompaniesIds.includes(id)) {
                    console.log(id);
                    this.companySelector.switchCompany("loginto", id);
                }
            });
        } else {
            // Select all companies
            this.isAllCompaniesSelected = true;
            this.allCompanyIds.forEach((id) => {
                if (!this.companySelector.selectedCompaniesIds.includes(id)) {
                    console.log(id);
                    this.companySelector.switchCompany("toggle", id);
                }
            });
        }
    },
});
