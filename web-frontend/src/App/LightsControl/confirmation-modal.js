import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Modal } from 'antd';

const ConfirmationModal = ({
  onConfirm,
  lightPlan,
  modalVisible,
  setModalVisible,
}) => {
  const [confirmLoading, setConfirmLoading] = useState(false);

  const handleOk = () => {
    setConfirmLoading(true);
    onConfirm().then(() => {
      setModalVisible(false);
      setConfirmLoading(false);
    });
  };

  const handleCancel = () => {
    console.log('Clicked cancel button');
    setModalVisible(false);
  };
  const startPlan = lightPlan[0];
  const startRange = [startPlan.on[0], startPlan.off[0]];

  return (
    <Modal
      title="Change lights cycle"
      visible={modalVisible}
      onOk={handleOk}
      confirmLoading={confirmLoading}
      onCancel={handleCancel}
    >
      <p>
        Lights will turn on at {startRange[0]}:00 and off at {startRange[1]}
        :00
      </p>
      <p>Total time on {startRange[1] - startRange[0]} hours.</p>
    </Modal>
  );
};

ConfirmationModal.propTypes = {
  onConfirm: PropTypes.func.isRequired,
  lightPlan: PropTypes.array,
  modalVisible: PropTypes.bool.isRequired,
  setModalVisible: PropTypes.func.isRequired,
};

export default ConfirmationModal;
