import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Modal } from 'antd';

const ConfirmationModal = ({
  onConfirm,
  lightsRange,
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

  return (
    <Modal
      title="Change lights cycle"
      visible={modalVisible}
      onOk={handleOk}
      confirmLoading={confirmLoading}
      onCancel={handleCancel}
    >
      <p>
        Lights will turn on at {lightsRange[0]}:00 and off at {lightsRange[1]}
        :00
      </p>
      <p>Total time on {lightsRange[1] - lightsRange[0]} hours.</p>
    </Modal>
  );
};

ConfirmationModal.propTypes = {
  onConfirm: PropTypes.func.isRequired,
  lightsRange: PropTypes.array,
  modalVisible: PropTypes.bool.isRequired,
  setModalVisible: PropTypes.func.isRequired,
};

export default ConfirmationModal;
