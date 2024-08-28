/**@odoo-module**/
import {SwitchCompanyMenu} from "@web/webclient/switch_company_menu/switch_company_menu";
import {patch} from "@web/core/utils/patch";

patch(SwitchCompanyMenu.prototype, {
    setup() {
        super.setup()
        this.allCompanyIds = Object.values(this.companyService.allowedCompanies).map(x => x.id);

        this.isAllCompaniesSelected = this.allCompanyIds.every((elem) =>
            this.companySelector.selectedCompaniesIds.includes(elem)
        );
    },

    toggleSelectAllCompanies() {
        if (!(this.isAllCompaniesSelected)) {
            this.isAllCompaniesSelected = true
            for (var id = 1; id < this.allCompanyIds.length + 1; id++) {
                if (!(this.companySelector.selectedCompaniesIds.includes(id))) {
                    console.log(id)
                    this.companySelector.switchCompany("toggle", id)
                }
            }
        } else {
            this.isAllCompaniesSelected = false
            for (var id = 1; id < this.allCompanyIds.length + 1; id++) {
                if ((this.companySelector.selectedCompaniesIds.includes(id))) {
                    console.log(id)
                    this.companySelector.switchCompany("loginto", id)
                }
            }
        }
    },
});
