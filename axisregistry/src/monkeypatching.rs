// STAT tables are *horrible*.

use fontations::skrifa::string::StringId;
use fontations::write::tables::stat::AxisValue as WriteAxisValue;

pub(crate) trait AxisValueNameId {
    fn value_name_id(&self) -> Option<StringId>;
}

pub(crate) trait SetAxisValueNameId {
    fn set_value_name_id(&mut self, value_name_id: StringId);
}

impl AxisValueNameId for WriteAxisValue {
    fn value_name_id(&self) -> Option<StringId> {
        match self {
            WriteAxisValue::Format1(value) => Some(value.value_name_id),
            WriteAxisValue::Format2(value) => Some(value.value_name_id),
            WriteAxisValue::Format3(value) => Some(value.value_name_id),
            WriteAxisValue::Format4(_) => None,
        }
    }
}

impl SetAxisValueNameId for WriteAxisValue {
    fn set_value_name_id(&mut self, value_name_id: StringId) {
        match self {
            WriteAxisValue::Format1(value) => value.value_name_id = value_name_id,
            WriteAxisValue::Format2(value) => value.value_name_id = value_name_id,
            WriteAxisValue::Format3(value) => value.value_name_id = value_name_id,
            WriteAxisValue::Format4(_) => {}
        }
    }
}
