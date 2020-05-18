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

  return (
    <Modal
      title="Confirm new lights cycle"
      visible={modalVisible}
      onOk={handleOk}
      confirmLoading={confirmLoading}
      onCancel={() => setModalVisible(false)}
    >
      {lightPlan.map((el, index) => (
        <div key={index}>
          <p>
            <b>{el.date === 'start' ? 'Beginning' : `From ${el.date}`}</b>
          </p>
          <p>
            Lights will turn <b>on</b> at {el.on[0]}:00 and <b>off</b> at{' '}
            {el.off[0]}
            :00.
          </p>
          <p>Total time on {el.off[0] - el.on[0]} hours.</p>
        </div>
      ))}
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
